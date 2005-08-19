#!/usr/bin/perl -w 

#----------------------------------------------------------------------
# copyright (C) 2004 Shad L. Lords <slords@mail.com>
# Copyright (C) 2005 Gordon Rowell <gordonr@gormand.com.au>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 		
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 		
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
#----------------------------------------------------------------------

package esmith::FormMagick::Panel::clamav;

use strict;
use esmith::ConfigDB;
use esmith::FormMagick;
use CGI::FormMagick::TagMaker;
use esmith::util;
use esmith::cgi;
use File::Basename;
use File::stat;
use Exporter;
use Carp;

our @ISA = qw(esmith::FormMagick Exporter);

our @EXPORT = qw(
        get_prop get_value 
        change_settings domain_name_or_ip portnumber
        );

our $VERSION = sprintf '%d.%03d', q$Revision: 1.3 $ =~ /: (\d+).(\d+)/;
our $db = esmith::ConfigDB->open 
|| warn "Couldn't open configuration database (permissions problems?)";

=pod 

=head1 NAME

esmith::FormMagick::Panels::clamav - useful panel functions

=head1 SYNOPSIS

use esmith::FormMagick::Panels::clamav;

my $panel = esmith::FormMagick::Panel::clamav->new();
$panel->display();

=head1 DESCRIPTION

=cut

=head2 new();

Exactly as for esmith::FormMagick

=cut

sub new {
    shift;
    my $self = esmith::FormMagick->new();
    $self->{calling_package} = (caller)[0];
    bless $self;
    return $self;
}

=head2 get_prop ITEM PROP

A simple accessor for esmith::ConfigDB::Record::prop

=cut

sub get_prop {
    my ($fm, $item, $prop, $default) = @_;
    warn "You must specify a record key"    unless $item;
    warn "You must specify a property name" unless $prop;
    my $record = $db->get($item) or warn "Couldn't get record for $item";
    my $value = $record ? $record->prop($prop) : undef;
    return defined $value ? $value : $default;
}

=head2 get_value ITEM

A simple accessor for esmith::ConfigDB::Record::value

=cut

sub get_value {
    my ($fm,$item,$default) = @_;
    my $record = $db->get($item) or warn "Couldn't get record for $item";
    my $value = $record ? $record->value() : undef;
    return defined $value ? $value : $default;
}

sub change_settings {
    my ($fm) = @_;
    my $q = $fm->{'cgi'};

    my $status = $q->param('status');

    my $FilesystemScan = ( $q->param('FilesystemScan') || 'disabled' );
    my $Quarantine = ( $q->param('Quarantine') || 'disabled' );

    my $DatabaseMirror = ( $q->param('DatabaseMirror') || 'db.us.clamav.net' );
    my $UpdateOfficeHrs = ( $q->param('UpdateOfficeHrs') || 'disabled' );
    my $UpdateNonOfficeHrs = ( $q->param('UpdateNonOfficeHrs') || 'disabled' );
    my $UpdateWeekend = ( $q->param('UpdateWeekend') || 'disabled' );

    my $HTTPProxyServer = ( $q->param('HTTPProxyServer') || '' );
    my $HTTPProxyPort = ( $q->param('HTTPProxyPort') || '' );
    my $HTTPProxyUsername = ( $q->param('HTTPProxyUsername') || '' );
    my $HTTPProxyPassword = ( $q->param('HTTPProxyPassword') || '' );

    my $clamav = $db->get('clamav') || $db->new_record('clamav', {type=>'service'});
    $status ||= $clamav->prop('status');

    $clamav->merge_props(
	    status => $status,
	    FilesystemScan => $FilesystemScan,
	    Quarantine => $Quarantine,
	    DatabaseMirror => $DatabaseMirror,
	    UpdateOfficeHrs => $UpdateOfficeHrs,
	    UpdateNonOfficeHrs => $UpdateNonOfficeHrs,
	    UpdateWeekend => $UpdateWeekend,
	    HTTPProxyServer => $HTTPProxyServer,
	    HTTPProxyPort => $HTTPProxyPort,
	    HTTPProxyUsername => $HTTPProxyUsername,
	    HTTPProxyPassword => $HTTPProxyPassword,
	);

    return $fm->error('ERROR_UPDATING')
        unless ( system( "/sbin/e-smith/signal-event", "clamav-update" ) == 0 );

    $fm->success('SUCCESS');
}

sub get_clam_versions
{
    my ($fm) = @_;

    my $version = `/usr/bin/clamscan -V`;
    chomp $version;
    $version =~ s/^ClamAV //;
 
    return $version;
}

sub domain_name_or_ip {
    my ($fm, $data) = @_;

    return 'OK' unless $data;
    my $response = $fm->domain_name($data);
    $response = $fm->ip_number($data) unless ($response eq 'OK');
    $response = 'INVALID_PROXY_SERVER' unless ($response eq 'OK');
    return $response;
}

sub portnumber
{
    my ($fm, $data) = @_;

    return 'OK' unless $data;
    my $response = $fm->number($data);
    $response = 'INVALID_PORT_NUMBER' unless ($response eq 'OK');
    return $response;
}

sub show_proxy_settings
{
    my ($fm, $data) = @_;

    return (($db->get_prop("clamav", "ShowProxySettings") || "no") eq "yes");
}

sub show_update_settings
{
    my ($fm, $data) = @_;

    return (($db->get_prop("clamav", "ShowUpdateSettings") || "no") eq "yes");
}

1;


