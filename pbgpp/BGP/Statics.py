#
# This file is part of PCAP BGP Parser (pbgpp)
#
# Copyright 2016 DE-CIX Management GmbH
# Author: Tobias Hannaske <tobias.hannaske@de-cix.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class BGPStatics:
    # ** BGPMessage **
    # Message types according to RFC 4271
    ##
    MESSAGE_TYPE_RESERVED = 0
    MESSAGE_TYPE_OPEN = 1
    MESSAGE_TYPE_UPDATE = 2
    MESSAGE_TYPE_NOTIFICATION = 3
    MESSAGE_TYPE_KEEPALIVE = 4
    MESSAGE_TYPE_ROUTE_REFRESH = 5

    # ** BGPUpdate sub-types **
    # Internal Usage Only
    ##
    UPDATE_TYPE_NONE = 0x0
    UPDATE_TYPE_ANNOUNCE = 0x1
    UPDATE_TYPE_WITHDRAWAL = 0x2
    UPDATE_TYPE_BOTH = 0x3

    # ** BGPOpen **
    # Optional parameters according to RFC 5492 and RFC 4271
    # Unassigned: 3-255
    ##
    OPEN_RESERVED = 0
    OPEN_AUTHENTICATION = 1 # (Deprecated)
    OPEN_CAPABILITY = 2

    # ** BGPOpenOptionalParameterCapability sub-codes **
    ##
    CAPABILITY_UNKNOWN = -1
    CAPABILITY_RESERVED = 0
    CAPABILITY_MULTIPROTOCOL_EXTENSIONS = 1
    CAPABILITY_ROUTE_REFRESH = 2
    CAPABILITY_OUTBOUND_ROUTE_FILTERING = 3
    CAPABILITY_MULTIPLE_ROUTES_TO_DESTINATION = 4
    CAPABILITY_EXTENDED_NEXT_HOP_ENCODING = 5
    CAPABILITY_BGP_EXTENDED = 6
    CAPABILITY_GRACEFUL_RESTART = 64
    CAPABILITY_SUPPORT_FOR_FOUR_OCTET_AS = 65
    CAPABILITY_SUPPORT_FOR_DYNAMIC_CAPABILITY = 67
    CAPABILITY_MULTISESSION_BGP = 68
    CAPABILITY_ADD_PATH = 69
    CAPABILITY_ENHANCED_ROUTE_REFRESH = 70
    CAPABILITY_LONG_LIVED_GRACEFUL_RESTART = 71
    CAPABILITY_FQDN = 73
    CAPABILITY_ALTERNATIVE_ROUTE_REFRESH = 128

    # ** BGPUpdate **
    # Path attributes according to RFC 4271
    # Unassigned: 30-39 && 41-127 && 129-254
    # Temporary: 40 (Until 2016-09-30)
    ##
    UPDATE_ATTRIBUTE_RESERVED = 0
    UPDATE_ATTRIBUTE_ORIGIN = 1
    UPDATE_ATTRIBUTE_AS_PATH = 2
    UPDATE_ATTRIBUTE_NEXT_HOP = 3
    UPDATE_ATTRIBUTE_MULTI_EXIT_DISC = 4
    UPDATE_ATTRIBUTE_LOCAL_PREF = 5
    UPDATE_ATTRIBUTE_ATOMIC_AGGREGATE = 6
    UPDATE_ATTRIBUTE_AGGREGATOR = 7
    UPDATE_ATTRIBUTE_COMMUNITIES = 8
    UPDATE_ATTRIBUTE_ORIGINATOR_ID = 9
    UPDATE_ATTRIBUTE_CLUSTER_LIST = 10
    UPDATE_ATTRIBUTE_DPA = 11 # (Deprecated)
    UPDATE_ATTRIBUTE_ADVERTISER = 12 # (Historic) (Depcrecated)
    UPDATE_ATTRIBUTE_RCID_PATH_CLUSTER_ID = 13 # (Historic) (Deprecated)
    UPDATE_ATTRIBUTE_MP_REACH_NLRI = 14
    UPDATE_ATTRIBUTE_MP_UNREACH_NLRI = 15
    UPDATE_ATTRIBUTE_EXTENDED_COMMUNITIES = 16
    UPDATE_ATTRIBUTE_AS4_PATH = 17
    UPDATE_ATTRIBUTE_AS4_AGGREGATOR = 18
    UPDATE_ATTRIBUTE_SAFI_SSA = 19 # (Deprecated)
    UPDATE_ATTRIBUTE_CONNECTOR_ATTRIBUTE = 20 # (Deprecated)
    UPDATE_ATTRIBUTE_AS_PATHLIMIT = 21 # (Deprecated)
    UPDATE_ATTRIBUTE_PMSI_TUNNEL = 22
    UPDATE_ATTRIBUTE_TUNNEL_ENCAPSULATION = 23
    UPDATE_ATTRIBUTE_TRAFFIC_ENGINEERING = 24
    UPDATE_ATTRIBUTE_IPV6_ADDRESS_SPECIFIC_EXTENDED_COMMUNITY = 25
    UPDATE_ATTRIBUTE_AIGP = 26
    UPDATE_ATTRIBUTE_PE_DISTINGUISHER_LABLES = 27
    UPDATE_ATTRIBUTE_BGP_ENTROPY_LABEL_CAPABILITY = 28 # (Deprecated)
    UPDATE_ATTRIBUTE_BGP_LS = 29
    UPDATE_ATTRIBUTE_LARGE_COMMUNITIES = 32
    UPDATE_ATTRIBUTE_ATTR_SET = 128
    UPDATE_ATTRIBUTE_RESERVED_DEVELOPMENT = 255

    # ** BGPNotification **
    # BGP Error (Notification) Codes according to RFC 4271 and RFC 7313
    # Unassigned: 8-255
    ##
    NOTIFICATION_ERROR_RESERVED = 0
    NOTIFICATION_ERROR_MESSAGE_HEADER = 1
    NOTIFICATION_ERROR_OPEN_MESSAGE = 2
    NOTIFICATION_ERROR_UPDATE_MESSAGE = 3
    NOTIFICATION_ERROR_HOLD_TIMER_EXPIRED = 4
    NOTIFICATION_ERROR_FINITE_STATE_MACHINE = 5
    NOTIFICATION_ERROR_CEASE = 6
    NOTIFICATION_ERROR_ROUTE_REFRESH_MESSAGE = 7

    # NOTIFICATION_ERROR_MESSAGE_HEADER sub-codes
    # According to RFC 4493 and RFC 4271
    # Unassigned: 4-255
    ##
    NOTIFICATION_ERROR_MESSAGE_HEADER_UNSPECIFIC = 0
    NOTIFICATION_ERROR_MESSAGE_HEADER_CONNECTION_NOT_SYNCHRONIZED = 1
    NOTIFICATION_ERROR_MESSAGE_HEADER_BAD_MESSAGE_LENGTH = 2
    NOTIFICATION_ERROR_MESSAGE_HEADER_BAD_MESSAGE_TYPE = 3

    # NOTIFICATION_ERROR_OPEN_MESSAGE sub-codes
    # According to RFC 4493, RFC 4271 and RFC 5492
    # Unassigned: 5 && 8-255
    ##
    NOTIFICATION_ERROR_OPEN_MESSAGE_UNSPECIFIC = 0
    NOTIFICATION_ERROR_OPEN_MESSAGE_UNSUPPORTED_VERSION_NUMBER = 1
    NOTIFICATION_ERROR_OPEN_MESSAGE_BAD_PEER_AS = 2
    NOTIFICATION_ERROR_OPEN_MESSAGE_BAD_BGP_IDENTIFIER = 3
    NOTIFICATION_ERROR_OPEN_MESSAGE_UNSUPPORTED_OPTIONAL_PARAMETER = 4
    NOTIFICATION_ERROR_OPEN_MESSAGE_UNACCEPTABLE_HOLD_TIME = 6
    NOTIFICATION_ERROR_OPEN_MESSAGE_UNSUPPORTED_CAPABILITY = 7

    # NOTIFICATION_ERROR_UPDATE_MESSAGE sub-codes
    # According to RFC 4493 and RFC 4271
    # Unassigned: 7 && 12-255
    ##
    NOTIFICATION_ERROR_UPDATE_MESSAGE_UNSPECIFIC = 0
    NOTIFICATION_ERROR_UPDATE_MESSAGE_MALFORMED_ATTRIBUTE_LIST = 1
    NOTIFICATION_ERROR_UPDATE_MESSAGE_UNRECOGNIZED_WELL_KNOWN_ATTRIBUTE = 2
    NOTIFICATION_ERROR_UPDATE_MESSAGE_MISSING_WELL_KNOWN_ATTRIBUTE = 3
    NOTIFICATION_ERROR_UPDATE_MESSAGE_ATTRIBUTE_FLAGS_ERROR = 4
    NOTIFICATION_ERROR_UPDATE_MESSAGE_ATTRIBUTE_LENGTH_ERROR = 5
    NOTIFICATION_ERROR_UPDATE_MESSAGE_INVALID_ORIGIN_ATTRIBUTE = 6
    NOTIFICATION_ERROR_UPDATE_MESSAGE_INVALID_NEXT_HOP_ATTRIBUTE = 8
    NOTIFICATION_ERROR_UPDATE_MESSAGE_OPTIONAL_ATTRIBUTE_ERROR = 9
    NOTIFICATION_ERROR_UPDATE_MESSAGE_INVALID_NETWORK_FIELD = 10
    NOTIFICATION_ERROR_UPDATE_MESSAGE_MALFORMED_AS_PATH = 11

    # NOTIFICATION_ERROR_FINITE_STATE_MACHINE sub-codes
    # According to RFC 6608
    # Unassigned: 4-255
    ##
    NOTIFICATION_ERROR_FINITE_STATE_MACHINE_UNSPECIFIC = 0
    NOTIFICATION_ERROR_FINITE_STATE_MACHINE_UNEXPECTED_MESSAGE_OPENSENT = 1
    NOTIFICATION_ERROR_FINITE_STATE_MACHINE_UNEXPECTED_MESSAGE_OPENCONFIRM = 2
    NOTIFICATION_ERROR_FINITE_STATE_MACHINE_UNEXPECTED_MESSAGE_ESTABLISHED = 3

    # NOTIFICATION_ERROR_CEASE sub-codes
    # According to RFC 4486
    # Unassigned: 9-255
    ##
    NOTIFICATION_ERROR_CEASE_RESERVED = 0
    NOTIFICATION_ERROR_CEASE_MAXIMUM_NUMBERS_OF_PREFIXES_REACHED = 1
    NOTIFICATION_ERROR_CEASE_ADMINISTRATIVE_SHUTDOWN = 2
    NOTIFICATION_ERROR_CEASE_PEER_DECONFIGURED = 3
    NOTIFICATION_ERROR_CEASE_ADMINISTRATIVE_RESET = 4
    NOTIFICATION_ERROR_CEASE_CONNECTION_REJECTED = 5
    NOTIFICATION_ERROR_CEASE_OTHER_CONFIGURATION_CHANGE = 6
    NOTIFICATION_ERROR_CEASE_CONNECTION_COLLISION_RESOLUTION = 7
    NOTIFICATION_ERROR_CEASE_OUT_OF_RESOURCES = 8

    # NOTIFICATION_ERROR_ROUTE_REFRESH_MESSAGE sub-codes
    # According to RFC 7313
    # Unassgined: 2-255
    ##
    NOTIFICATION_ERROR_ROUTE_REFRESH_MESSAGE_RESERVED = 0
    NOTIFICATION_ERROR_ROUTE_REFRESH_MESSAGE_INVALID_MESSAGE_LENGTH = 1

    # ** BGP Outbound Route Filtering (ORF) Types **
    # According to RF 5291
    # Unassigned: 1-63 && 66-127
    # Registration Procedurs:
    # :: 0-63       - Standards Action
    # :: 64-127     - First Come First Served
    # :: 128-255    - Vendor-Specific
    ##
    ORF_RESERVED = 0
    ORF_ADDRESS_PREFIX = 64
    ORF_CP = 65

    # ** BGP Tunnel Encapsulation Attribute Tunnel Types **
    # According to RFC 5512 and RFC 5566
    # Unassigned: 15-65535
    ##
    TUNNEL_ENCAPSULATION_ATTRIBUTE_RESERVED = 0
    TUNNEL_ENCAPSULATION_ATTRIBUTE_L2TPV3_OVER_IP = 1
    TUNNEL_ENCAPSULATION_ATTRIBUTE_GRE = 2
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TRANSMIT_TUNNEL_ENDPOINT = 3
    TUNNEL_ENCAPSULATION_ATTRIBUTE_IPSEC_TUNNELMODE = 4
    TUNNEL_ENCAPSULATION_ATTRIBUTE_IP_IN_IP_TUNNEL_WITH_IPSEC_TRANSPORT_MODE = 5
    TUNNEL_ENCAPSULATION_ATTRIBUTE_MPLS_IN_IP_TUNNEL_WITH_IPSEC_TRANSPORT_MODE = 6
    TUNNEL_ENCAPSULATION_ATTRIBUTE_IP_IN_IP = 7
    TUNNEL_ENCAPSULATION_ATTRIBUTE_VXLAN = 8
    TUNNEL_ENCAPSULATION_ATTRIBUTE_NVGRE = 9
    TUNNEL_ENCAPSULATION_ATTRIBUTE_MPLS = 10
    TUNNEL_ENCAPSULATION_ATTRIBUTE_MPLS_IN_GRE = 11
    TUNNEL_ENCAPSULATION_ATTRIBUTE_VXLAN_GPE = 12
    TUNNEL_ENCAPSULATION_ATTRIBUTE_MPLS_UDP = 13
    TUNNEL_ENCAPSULATION_ATTRIBUTE_IPV6_TUNNEL = 14

    # ** TUNNEL_ENCAPSULATION_ATTRIBUTE sub-TLVS **
    # According to RFC 5512, RFC 5566 and RFC 5640
    # Unassigned: 6-255
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_RESERVED = 0
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_ENCAPSULATION = 1
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_PROTOCOL_TYPE = 2
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_IPSEC_TUNNEL_AUTH = 3
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_COLOR = 4
    TUNNEL_ENCAPSULATION_ATTRIBUTE_TLV_LOAD_BALANCING_BLOCK = 5

    # ** BGP Layer 2 Encapsulation Types **
    # According to RFC 6624, RFC 4446, RFC 4816, RFC 4618, RFC 4717,
    # RFC 3032, RFC 4619, RFC 4553, RFC 4761 and RFC 5086
    # Unassigned: 12-14 && 16 && 22-24 && 25-39 && 45-127 && 128-251
    # Registration procedures:
    # :: 0-127      - Expert Review
    # :: 128-251    - First Come First Served
    # :: 252-255    - Experimental Use
    ##
    LAYER2_ENCAPSULATION_RESERVED = 0
    LAYER2_ENCAPSULATION_FRAME_RELAY = 1
    LAYER2_ENCAPSULATION_ATM_AAL5_SDU_VCC_TRANSPORT = 2
    LAYER2_ENCAPSULATION_ATM_TRANSPARENT_CELL_TRANSPORT = 3
    LAYER2_ENCAPSULATION_ETHERNET_VLAN_TAGGED_MODE = 4
    LAYER2_ENCAPSULATION_ETHERNET_RAW_MODE = 5
    LAYER2_ENCAPSULATION_CISCO_HDLC = 6
    LAYER2_ENCAPSULATION_PPP = 7
    LAYER2_ENCAPSULATION_SONET_SDH_CIRCUIT_EMULATION_SERVICE = 8
    LAYER2_ENCAPSULATION_ATM_N_TO_ONE_VCC_CELL_TRANSPORT = 9
    LAYER2_ENCAPSULATION_ATM_N_TO_ONE_VPC_CELL_TRANSPORT = 10
    LAYER2_ENCAPSULATION_IP_LAYER2_TRANSPORT = 11
    LAYER2_ENCAPSULATION_FRAME_RELAY_PORT_MODE = 15
    LAYER2_ENCAPSULATION_STRUCTURE_AGNOSTIC_E1_OVER_PACKET = 17
    LAYER2_ENCAPSULATION_STRUCTURE_AGNOSTIC_T1_DS1_OVER_PACKET = 18
    LAYER2_ENCAPSULATION_VPLS = 19
    LAYER2_ENCAPSULATION_STRUCTURE_AGNOSTIC_T3_DS3_OVER_PACKET = 20
    LAYER2_ENCAPSULATION_NX64KBITS_BASIC_SERVICE_USING_STRUCTURE_AWARE = 21
    LAYER2_ENCAPSULATION_FRAME_RELAY_DLCI = 25
    LAYER2_ENCAPSULATION_STRUCTURE_AGNOSTIC_E3_OVER_PACKET = 40
    LAYER2_ENCAPSULATION_OCTET_ALIGNED_PAYLOAD_FOR_STRUCTURE_AGNOSTIC_DS1_CIRCUITS = 41
    LAYER2_ENCAPSULATION_E1_NX64KBITS_WITH_CAS_USING_STRUCTURE_AWARE = 42
    LAYER2_ENCAPSULATION_DS1_ESF_NX64KBITS_WITH_CAS_USING_STRUCTURE_AWARE = 43
    LAYER2_ENCAPSULATION_DS1_SF_NX64KBITS_WITH_CAS_USING_STRUCTURE_AWARE = 44

    # ** BGP Layer 2 TLV Types **
    # According to RFC 6624
    # Unassigned: 2-127 && 128-251
    # Registration procedures:
    # :: 0-127      - Expert Review
    # :: 128-251    - First Come First Served
    # :: 252-255    - Experimental Use
    ##
    LAYER2_TLV_RESERVED = 0
    LAYER2_TLV_CIRCUIT_STATUS_VECTOR = 1

    # ** BGP AIGP Attribute Types **
    # According to RFC 7311
    # Unassigned: 2-255
    ##
    AIGP_ATTRIBUTE_RESERVED = 0
    AIGP_ATTRIBUTE = 1

    # ** BGPKeepalive **
    ##
    KEEPALIVE_FIXED_LENGTH = 19 # (Every KEEPALIVE message must be 19 bytes long)

    # ** BGPRouteRefresh **
    # According to RFC 7313, RFC 2918 and RFC 5291
    # Unassigned: 3-254
    # Registration procedure:
    # :: 0-127      - Standards Action
    # :: 128-254    - First Come First Served
    ##
    ROUTE_REFRESH = 0
    ROUTE_REFRESH_BORR = 1
    ROUTE_REFRESH_EORR = 2

    # ** BGP P-Multicast Service Interface (PMSI) Tunnel Attribute Flags **
    # According to RFC 7902 and RFC 6514
    # Unassigned: 0 && 2
    # Temporary:
    # :: 3-4        - Assisted-Replication-Type (T) (Until: 2017-06-30)
    # :: 5          - Broadcast and Multicast (BM)  (Until: 2017-06-30)
    # :: 6          - Unknown (U)                   (Until: 2017-06-30)
    ##
    PMSI_TUNNEL_ATTRIBUTE_EXTENSION = 1
    PMSI_TUNNEL_ATTRIBUTE_LEAF_INFORMATION_REQUIRED = 7

    # ** BGPUpdate Flags **
    ##
    UPDATE_FLAG_LENGTH = 0x10
    UPDATE_FLAG_PARTIAL = 0x20
    UPDATE_FLAG_TRANSITIVE = 0x40
    UPDATE_FLAG_OPTIONAL = 0x80

    # ** BGPUpdate Path Attribute ORIGIN sub-codes **
    # According to RFC 4271
    ##
    ORIGIN_IGP = 0
    ORIGIN_EGP = 1
    ORIGIN_INCOMPLETE = 2

    # ** BGPUpdate Path Atribute AS_PATH sub-codes **
    # According to RFC 4271
    ##
    AS_PATH_SEGMENT_SET = 1
    AS_PATH_SEGMENT_SEQUENCE = 2

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES sub-types **
    # According to RFC 4360
    # NT = Non-Transitive
    # T = Transitive
    ##
    EXT_COMMUNITY_T_TWO_OCTET_AS_SPECIFIC = 0
    EXT_COMMUNITY_T_IPV4_ADDRESS_SPECIFIC = 1
    EXT_COMMUNITY_T_FOUR_OCTET_AS_SPECIFIC = 2
    EXT_COMMUNITY_T_OPAQUE = 3
    EXT_COMMUNITY_T_QOS_MARKING = 4
    EXT_COMMUNITY_T_COS_CAPABILITY = 5
    EXT_COMMUNITY_T_EVPN = 6
    EXT_COMMUNITY_T_FLOW_SPEC_REDIRECT_MIRROR_TO_IP_NEXT_HOP = 8
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_USE = 128
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_USE_PART2 = 129
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_USE_PART3 = 130

    EXT_COMMUNITY_NT_TWO_OCTET_AS_SPECIFIC = 64
    EXT_COMMUNITY_NT_IPV4_ADDRESS_SPECIFIC = 65
    EXT_COMMUNITY_NT_FOUR_OCTET_AS_SPECIFIC = 66
    EXT_COMMUNITY_NT_OPAQUE = 67
    EXT_COMMUNITY_NT_QOS_MARKING = 68

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES EVPN sub-types ***
    # According to RFC 7153
    ##
    EXT_COMMUNITY_EVPN_MAC_MOBILITY = 0
    EXT_COMMUNITY_EVPN_ESI_LABEL = 1
    EXT_COMMUNITY_EVPN_ES_IMPORT_ROUTE_TARGET = 2
    EXT_COMMUNITY_EVPN_ROUTERS_MAC = 3
    EXT_COMMUNITY_EVPN_LAYER2 = 4
    EXT_COMMUNITY_EVPN_ETREE = 5
    EXT_COMMUNITY_EVPN_DF_ELECTION = 6
    EXT_COMMUNITY_EVPN_ISID = 7

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Two-Octet AS-Specific **
    # According to RFC 4360, RFC 4577, RFC 4384, RFC 6514 and RFC 6074
    ##
    EXT_COMMUNITY_T_TWO_OCTET_AS_ROUTE_TARGET = 2
    EXT_COMMUNITY_T_TWO_OCTET_AS_ROUTE_ORIGIN = 3
    EXT_COMMUNITY_T_TWO_OCTET_AS_OSPF_DOMAIN_IDENTIFIER = 5
    EXT_COMMUNITY_T_TWO_OCTET_AS_BGP_DATA_COLLECTION = 8
    EXT_COMMUNITY_T_TWO_OCTET_AS_SOURCE_AS = 9
    EXT_COMMUNITY_T_TWO_OCTET_AS_L2VPN_IDENTIFIER = 10
    EXT_COMMUNITY_T_TWO_OCTET_AS_CISCO_VPN_DISTINGUISHER = 16
    EXT_COMMUNITY_T_TWO_OCTET_AS_ROUTE_TARGET_RECORD = 19

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES non-trans. Two-Octet AS-Specific **
    ##
    EXT_COMMUNITY_NT_TWO_OCTET_AS_LINK_BANDWIDTH = 4
    EXT_COMMUNITY_NT_TWO_OCTET_AS_VIRTUAL_NETWORK_IDENTIFIER = 128

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Four-Octet AS-Specific **
    # According to RFC 5668, RFC 4577, RFC 4384 and RFC 6514
    ##
    EXT_COMMUNITY_T_FOUR_OCTET_AS_ROUTE_TARGET = 2
    EXT_COMMUNITY_T_FOUR_OCTET_AS_ROUTE_ORIGIN = 3
    EXT_COMMUNITY_T_FOUR_OCTET_AS_GENERIC = 4
    EXT_COMMUNITY_T_FOUR_OCTET_AS_OSPF_DOMAIN_IDENTIFIER = 5
    EXT_COMMUNITY_T_FOUR_OCTET_AS_BGP_DATA_COLLECTION = 8
    EXT_COMMUNITY_T_FOUR_OCTET_AS_SOURCE_AS = 9
    EXT_COMMUNITY_T_FOUR_OCTET_AS_CISCO_VPN_IDENTIFIER = 16
    EXT_COMMUNITY_T_FOUR_OCTET_AS_ROUTE_TARGET_RECORD = 19

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES non-trans. Four-Octet AS-Specific **
    ##
    EXT_COMMUNITY_NT_FOUR_OCTET_AS_GENERIC = 4

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. IPv4-Address-Specific **
    # According to RFC 4360, RFC 4577, RFC 6074, RFC 6541 and RFC 7524
    ##
    EXT_COMMUNITY_T_IPV4_ADDRESS_ROUTE_TARGET = 2
    EXT_COMMUNITY_T_IPV4_ADDRESS_ROUTE_ORIGIN = 3
    EXT_COMMUNITY_T_IPV4_ADDRESS_OSPF_DOMAIN_IDENTIFIER = 5
    EXT_COMMUNITY_T_IPV4_ADDRESS_OSPF_ROUTE_ID = 7
    EXT_COMMUNITY_T_IPV4_ADDRESS_L2VPN_IDENTIFIER = 10
    EXT_COMMUNITY_T_IPV4_ADDRESS_VRF_ROUTE_IMPORT = 11
    EXT_COMMUNITY_T_IPV4_ADDRESS_FLOW_SPEC_REDIRECT_TO_IPV4 = 12
    EXT_COMMUNITY_T_IPV4_ADDRESS_CISCO_VPN_DISTINGUISHER = 16
    EXT_COMMUNITY_T_IPV4_ADDRESS_INTER_AREA_P2MP_SEGMENTED_NEXT_HOP = 18
    EXT_COMMUNITY_T_IPV4_ADDRESS_ROUTE_TARGET_RECORD = 19

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Opaque **
    ##
    EXT_COMMUNITY_T_OPAQUE_COST_COMMUNITY = 1
    EXT_COMMUNITY_T_OPAQUE_CP_ORF = 3
    EXT_COMMUNITY_T_OPAQUE_EXTRANET_SOURCE = 4
    EXT_COMMUNITY_T_OPAQUE_EXTRANET_SEPARATION = 5
    EXT_COMMUNITY_T_OPAQUE_OSPF_ROUTE_TYPE = 6
    EXT_COMMUNITY_T_OPAQUE_ADDITIONAL_PMSI_TUNNEL_ATTRIBUTE_FLAGS = 7
    EXT_COMMUNITY_T_OPAQUE_COLOR_EXTENDED = 11
    EXT_COMMUNITY_T_OPAQUE_ENCAPSULATION = 12
    EXT_COMMUNITY_T_OPAQUE_DEFAULT_GATEWAY = 13
    EXT_COMMUNITY_T_OPAQUE_PPMP_LABEL = 14
    EXT_COMMUNITY_T_OPAQUE_CONSISTENT_HASH_SORT_ORDER = 20

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES non-trans. Opaque **
    ##
    EXT_COMMUNITY_NT_OPAQUE_BGP_ORIGIN_VALIDATION_STATE = 0
    EXT_COMMUNITY_NT_OPAQUE_COST_COMMUNITY = 1

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Generic Experimental **
    ##
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_OSPF_ROUTE_TYPE = 0
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_OSPF_ROUTER_ID = 1
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_OSPF_DOMAIN_IDENTIFIER = 5
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_FLOW_SPEC_TRAFFIC_RATE = 6
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_FLOW_SPEC_TRAFFIC_ACTION = 7
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_FLOW_SEPC_REDIRECT_AS_2BYTE_FORMAT = 8
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_FLOW_SPEC_TRAFFIC_REMARKING = 9
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_LAYER2_INFO = 10
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_E_TREE_INFO = 11

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Generic Experimental Part 2 **
    ##
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_PART2_FLOW_SPEC_REDIRECT_IPV4_FORMAT = 8

    # ** BGPUpdate Path Attribute EXTENDED_COMMUNITIES trans. Generic Experimental Part 3 **
    EXT_COMMUNITY_T_GENERIC_EXPERIMENTAL_PART3_FLOW_SPEC_AS_4BYTE_FORMAT = 8
