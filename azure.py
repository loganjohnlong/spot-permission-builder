import json

################
# GLOBAL VARIABLES
################

## NOTE: The '*full_access' lists only contain the additional permissions needed to go from read only to full access. They cannot be used as-is.
core_read_only = [
    "Microsoft.Authorization/roleAssignments/read",
    "Microsoft.Compute/galleries/images/read",
    "Microsoft.Compute/galleries/images/versions/read",
    "Microsoft.Compute/galleries/read",
    "Microsoft.Compute/disks/read",
    "Microsoft.Compute/images/read",
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Insights/MetricDefinitions/Read",
    "Microsoft.Insights/Metrics/Read",
    "Microsoft.ManagedIdentity/userAssignedIdentities/read",
    "Microsoft.ManagedIdentity/identities/read",
    "Microsoft.Network/networkInterfaces/read",
    "Microsoft.Network/networkSecurityGroups/read",
    "Microsoft.Network/networkInterfaces/ipconfigurations/read",
    "Microsoft.Network/publicIPAddresses/read",
    "Microsoft.Network/routeTables/read",
    "Microsoft.Network/virtualNetworks/read",
    "Microsoft.Network/virtualNetworks/subnets/read",
    "Microsoft.Network/virtualNetworks/virtualMachines/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
]

core_full_access = [
    "Microsoft.Compute/disks/write",
    "Microsoft.Compute/disks/delete",
    "Microsoft.Compute/virtualMachines/*",
    "Microsoft.ManagedIdentity/userAssignedIdentities/assign/action",
    "Microsoft.Network/networkInterfaces/write",
    "Microsoft.Network/networkInterfaces/delete",
    "Microsoft.Network/networkInterfaces/join/action",
    "Microsoft.Network/networkSecurityGroups/join/action",
    "Microsoft.Network/publicIPAddresses/write",
    "Microsoft.Network/publicIPAddresses/delete",
    "Microsoft.Network/publicIPAddresses/join/action",
    "Microsoft.Network/virtualNetworks/subnets/join/action",
    "Microsoft.Network/virtualNetworks/subnets/write",
    "Microsoft.KeyVault/vaults/deploy/action",
    "Microsoft.Resources/tags/write",
]

eco_read_only = [
    "Microsoft.Authorization/roleAssignments/read",
    "Microsoft.Advisor/advisorScore/read",
    "Microsoft.Capacity/catalogs/read",
    "Microsoft.Capacity/register/action",
    "Microsoft.Compute/register/action",
    "Microsoft.Compute/capacityReservationGroups/read",
    "Microsoft.Compute/operations/read",
    "Microsoft.Compute/availabilitySets/vmSizes/read",
    "Microsoft.Compute/availabilitySets/read",
    "Microsoft.Compute/capacityReservationGroups/capacityReservations/read",
    "Microsoft.Compute/locations/capsOperations/read",
    "Microsoft.Compute/cloudServices/instanceView/read",
    "Microsoft.Compute/cloudServices/providers/Microsoft.Insights/metricDefinitions/read",
    "Microsoft.Compute/cloudServices/roles/providers/Microsoft.Insights/metricDefinitions/read",
    "Microsoft.Compute/locations/publishers/artifacttypes/offers/skus/read",
    "Microsoft.Compute/skus/read",
    "Microsoft.Compute/locations/usages/read",
    "Microsoft.Compute/virtualMachineScaleSets/vmSizes/read",
    "Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read",
    "Microsoft.Compute/locations/vmSizes/read",
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Compute/virtualMachines/vmSizes/read",
    "Microsoft.Consumption/register/action",
    "Microsoft.Consumption/reservationRecommendations/read",
    "Microsoft.CostManagement/query/action",
    "Microsoft.CostManagement/reports/action",
    "Microsoft.CostManagement/exports/action",
    "Microsoft.CostManagement/register/action",
    "Microsoft.CostManagement/views/action",
    "Microsoft.CostManagement/forecast/action",
    "Microsoft.CostManagement/alerts/read",
    "Microsoft.CostManagement/cloudConnectors/read",
    "Microsoft.CostManagement/dimensions/read",
    "Microsoft.CostManagement/exports/read",
    "Microsoft.CostManagement/exports/write",
    "Microsoft.CostManagement/exports/delete",
    "Microsoft.CostManagement/exports/run/action",
    "Microsoft.CostManagement/externalBillingAccounts/read",
    "Microsoft.CostManagement/externalBillingAccounts/query/action",
    "Microsoft.CostManagement/externalBillingAccounts/forecast/action",
    "Microsoft.CostManagement/externalBillingAccounts/dimensions/read",
    "Microsoft.CostManagement/externalBillingAccounts/query/read",
    "Microsoft.CostManagement/externalBillingAccounts/externalSubscriptions/read",
    "Microsoft.CostManagement/externalBillingAccounts/forecast/read",
    "Microsoft.CostManagement/externalSubscriptions/read",
    "Microsoft.CostManagement/externalSubscriptions/query/action",
    "Microsoft.CostManagement/externalSubscriptions/forecast/action",
    "Microsoft.CostManagement/externalSubscriptions/dimensions/read",
    "Microsoft.CostManagement/externalSubscriptions/query/read",
    "Microsoft.CostManagement/externalSubscriptions/forecast/read",
    "Microsoft.CostManagement/forecast/read",
    "Microsoft.CostManagement/operations/read",
    "Microsoft.CostManagement/query/read",
    "Microsoft.CostManagement/reports/read",
    "Microsoft.CostManagement/views/read",
    "Microsoft.CostManagement/views/delete",
    "Microsoft.CostManagement/views/write",
    "Microsoft.CostManagement/tenants/register/action",
    "Microsoft.CostManagement/budgets/read",
    "Microsoft.Insights/MetricDefinitions/Read",
    "Microsoft.Insights/Metrics/Read",
    "Microsoft.Resources/tags/read",
    "Microsoft.Resources/subscriptions/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.SQL/register/action",
]

eco_full_access = [
    "Microsoft.Advisor/generateRecommendations/action",
    "Microsoft.Advisor/register/action",
    "Microsoft.Advisor/unregister/action",
    "Microsoft.Advisor/configurations/read",
    "Microsoft.Advisor/configurations/write",
    "Microsoft.Advisor/generateRecommendations/read",
    "Microsoft.Advisor/operations/read",
    "Microsoft.Advisor/recommendations/read",
    "Microsoft.Advisor/recommendations/available/action",
    "Microsoft.Advisor/recommendations/suppressions/read",
    "Microsoft.Advisor/recommendations/suppressions/write",
    "Microsoft.Advisor/recommendations/suppressions/delete",
    "Microsoft.Support/supportTickets/read",
    "Microsoft.Support/supportTickets/write",
]

elastigroup_read_only = [
    "Microsoft.Compute/virtualMachineScaleSets/read",
    "Microsoft.Compute/virtualMachineScaleSets/instanceView/read",
    "Microsoft.Compute/virtualMachineScaleSets/networkInterfaces/read",
    "Microsoft.Compute/virtualMachineScaleSets/publicIPAddresses/read",
    "Microsoft.Compute/virtualMachineScaleSets/virtualMachines/extensions/read",
    "Microsoft.Insights/AutoscaleSettings/Read",
    "Microsoft.Insights/AutoscaleSettings/providers/Microsoft.Insights/MetricDefinitions/Read",
    "Microsoft.Compute/availabilitySets/read",
    "Microsoft.Compute/availabilitySets/vmSizes/read",
]

# Contained in core permissions, but kept here for logic clarity
elastigroup_full_access = []

ocean_read_only = [
    "Microsoft.ContainerService/managedClusters/read",
    "Microsoft.ContainerService/managedClusters/agentPools/read",
    "Microsoft.Compute/diskEncryptionSets/read",
    "Microsoft.Network/applicationGateways/read",
    "Microsoft.OperationalInsights/workspaces/sharedkeys/read",
    "Microsoft.OperationalInsights/workspaces/read",
    "Microsoft.OperationsManagement/solutions/read",
]

ocean_full_access = [
    "Microsoft.Compute/proximityPlacementGroups/write",
    "Microsoft.Network/applicationGateways/write",
    "Microsoft.Network/publicIPPrefixes/join/action",
    "Microsoft.OperationsManagement/solutions/write",
    "Microsoft.ManagedIdentity/userAssignedIdentities/assign/action",
    "Microsoft.Network/virtualNetworks/joinLoadBalancer/action",
]

netapp_storage_read_only = [
    "Microsoft.NetApp/netAppAccounts/read",
    "Microsoft.NetApp/netAppAccounts/capacityPools/read",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/read",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots/read",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/ReplicationStatus/read",
]

netapp_storage_full_access = [
    "Microsoft.NetApp/netAppAccounts/write",
    "Microsoft.NetApp/netAppAccounts/capacityPools/write",
    "Microsoft.NetApp/netAppAccounts/capacityPools/delete",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/write",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/delete",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots/write",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/DeleteReplication/action",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/ResyncReplication/action",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/AuthorizeReplication/action",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/ReInitializeReplication/action",
    "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/BreakReplication/action",
]

load_balancer_read_only = [
    "Microsoft.Network/loadBalancers/read",
    "Microsoft.Network/loadBalancers/backendAddressPools/read",
]

load_balancer_full_access = [
    "Microsoft.Network/loadBalancers/backendAddressPools/write",
    "Microsoft.Network/loadBalancers/backendAddressPools/join/action",
]

dns_read_only = [
    "Microsoft.Network/dnsZones/read",
    "Microsoft.Network/dnsZones/A/read",
]

dns_full_access = [
    "Microsoft.Network/dnsZones/write",
    "Microsoft.Network/dnsZones/A/write",
    "Microsoft.Network/dnsZones/A/delete",
]

app_gateways_read_only = [
    "Microsoft.Network/applicationGateways/read",
]

app_gateways_full_access = [
    "Microsoft.Network/applicationGateways/backendhealth/action",
    "Microsoft.Network/applicationGateways/backendAddressPools/join/action",
]

application_security_groups_read_only = [
    "Microsoft.Network/applicationSecurityGroups/read",
]

application_security_groups_full_access = [
    "Microsoft.Network/applicationSecurityGroups/joinIpConfiguration/action",
]

stateful_read_only = [
    "Microsoft.Compute/snapshots/read",
]

stateful_full_access = [
    "Microsoft.Compute/disks/beginGetAccess/action",
    "Microsoft.Compute/images/write",
    "Microsoft.Compute/snapshots/write",
    "Microsoft.Compute/snapshots/delete",
]

################
# HELPER FUNCTIONS
################
def inject_permission(role_def, permissions_ro, permissions_full, readonly):
    if readonly:
        role_def["properties"]["permissions"][0]["actions"] += permissions_ro
    else:
        role_def["properties"]["permissions"][0]["actions"] += (
            permissions_ro + permissions_full
        )
    return role_def


################
# MAIN FUNCTION
################
def generate_azure_config(
    products,
    readonly,
    netapp_storage,
    load_balancer,
    dns,
    app_gateways,
    application_security_groups,
    stateful,
    subscription_ids,
):

    role_definition = {
        "properties": {
            "roleName": "spotCustomRole_1671757595495",
            "isCustom": True,
            "description": "Custom Role for Spot Account.",
            "assignableScopes": [],
            "permissions": [
                {
                    "actions": [],
                    "notActions": [],
                    "dataActions": [],
                    "notDataActions": [],
                }
            ],
        }
    }

    # inject list of subscriptions
    role_definition["properties"]["assignableScopes"] += [
        "/subscriptions/" + sub for sub in subscription_ids
    ]

    # inject core permissions
    role_definition = inject_permission(
        role_definition, core_read_only, core_full_access, readonly
    )

    if "Eco" in products:
        # inject Eco permissions
        role_definition = inject_permission(
            role_definition, eco_read_only, eco_full_access, readonly
        )
    elif "Elastigroup" in products:
        # inject Elastigroup permissions
        role_definition = inject_permission(
            role_definition, elastigroup_read_only, elastigroup_full_access, readonly
        )
    elif "Ocean" in products:
        # inject Ocean permissions
        role_definition = inject_permission(
            role_definition, ocean_read_only, ocean_full_access, readonly
        )

    # inject NetApp Storage permissions
    role_definition = (
        inject_permission(
            role_definition,
            netapp_storage_read_only,
            netapp_storage_full_access,
            readonly,
        )
        if netapp_storage
        else role_definition
    )

    # inject Load Balancer permissions
    role_definition = (
        inject_permission(
            role_definition,
            load_balancer_read_only,
            load_balancer_full_access,
            readonly,
        )
        if load_balancer
        else role_definition
    )

    # inject DNS permissions
    role_definition = (
        inject_permission(role_definition, dns_read_only, dns_full_access, readonly)
        if dns
        else role_definition
    )

    # inject App Gateways permissions
    role_definition = (
        inject_permission(
            role_definition, app_gateways_read_only, app_gateways_full_access, readonly
        )
        if app_gateways
        else role_definition
    )

    # inject Application Security Groups permissions
    role_definition = (
        inject_permission(
            role_definition,
            application_security_groups_read_only,
            application_security_groups_full_access,
            readonly,
        )
        if application_security_groups
        else role_definition
    )

    # inject Stateful permissions
    role_definition = (
        inject_permission(
            role_definition, stateful_read_only, stateful_full_access, readonly
        )
        if stateful
        else role_definition
    )

    return json.dumps(role_definition, indent=4)
