# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ExpressRouteCircuitPeering(SubResource):
    """Peering in an ExpressRouteCircuit resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param peering_type: The PeeringType. Possible values are:
     'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'.
     Possible values include: 'AzurePublicPeering', 'AzurePrivatePeering',
     'MicrosoftPeering'
    :type peering_type: str or :class:`ExpressRouteCircuitPeeringType
     <azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeeringType>`
    :param state: The state of peering. Possible values are: 'Disabled' and
     'Enabled'. Possible values include: 'Disabled', 'Enabled'
    :type state: str or :class:`ExpressRouteCircuitPeeringState
     <azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeeringState>`
    :param azure_asn: The Azure ASN.
    :type azure_asn: int
    :param peer_asn: The peer ASN.
    :type peer_asn: int
    :param primary_peer_address_prefix: The primary address prefix.
    :type primary_peer_address_prefix: str
    :param secondary_peer_address_prefix: The secondary address prefix.
    :type secondary_peer_address_prefix: str
    :param primary_azure_port: The primary port.
    :type primary_azure_port: str
    :param secondary_azure_port: The secondary port.
    :type secondary_azure_port: str
    :param shared_key: The shared key.
    :type shared_key: str
    :param vlan_id: The VLAN ID.
    :type vlan_id: int
    :param microsoft_peering_config: The Microsoft peering configuration.
    :type microsoft_peering_config: :class:`ExpressRouteCircuitPeeringConfig
     <azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeeringConfig>`
    :param stats: Gets peering stats.
    :type stats: :class:`ExpressRouteCircuitStats
     <azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitStats>`
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param gateway_manager_etag: The GatewayManager Etag.
    :type gateway_manager_etag: str
    :param last_modified_by: Gets whether the provider or the customer last
     modified the peering.
    :type last_modified_by: str
    :param route_filter: The reference of the RouteFilter resource.
    :type route_filter: :class:`RouteFilter
     <azure.mgmt.network.v2017_06_01.models.RouteFilter>`
    :param ipv6_peering_config: The IPv6 peering configuration.
    :type ipv6_peering_config: :class:`Ipv6ExpressRouteCircuitPeeringConfig
     <azure.mgmt.network.v2017_06_01.models.Ipv6ExpressRouteCircuitPeeringConfig>`
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'peering_type': {'key': 'properties.peeringType', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_asn': {'key': 'properties.azureASN', 'type': 'int'},
        'peer_asn': {'key': 'properties.peerASN', 'type': 'int'},
        'primary_peer_address_prefix': {'key': 'properties.primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'properties.secondaryPeerAddressPrefix', 'type': 'str'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'microsoft_peering_config': {'key': 'properties.microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'stats': {'key': 'properties.stats', 'type': 'ExpressRouteCircuitStats'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'gateway_manager_etag': {'key': 'properties.gatewayManagerEtag', 'type': 'str'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'route_filter': {'key': 'properties.routeFilter', 'type': 'RouteFilter'},
        'ipv6_peering_config': {'key': 'properties.ipv6PeeringConfig', 'type': 'Ipv6ExpressRouteCircuitPeeringConfig'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, peering_type=None, state=None, azure_asn=None, peer_asn=None, primary_peer_address_prefix=None, secondary_peer_address_prefix=None, primary_azure_port=None, secondary_azure_port=None, shared_key=None, vlan_id=None, microsoft_peering_config=None, stats=None, provisioning_state=None, gateway_manager_etag=None, last_modified_by=None, route_filter=None, ipv6_peering_config=None, name=None):
        super(ExpressRouteCircuitPeering, self).__init__(id=id)
        self.peering_type = peering_type
        self.state = state
        self.azure_asn = azure_asn
        self.peer_asn = peer_asn
        self.primary_peer_address_prefix = primary_peer_address_prefix
        self.secondary_peer_address_prefix = secondary_peer_address_prefix
        self.primary_azure_port = primary_azure_port
        self.secondary_azure_port = secondary_azure_port
        self.shared_key = shared_key
        self.vlan_id = vlan_id
        self.microsoft_peering_config = microsoft_peering_config
        self.stats = stats
        self.provisioning_state = provisioning_state
        self.gateway_manager_etag = gateway_manager_etag
        self.last_modified_by = last_modified_by
        self.route_filter = route_filter
        self.ipv6_peering_config = ipv6_peering_config
        self.name = name
        self.etag = None
