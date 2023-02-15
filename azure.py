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

def inject_scope(subscription_id, role_definition):
    role_definition["properties"]["assignableScopes"] += ["/subscriptions/" + subscription_id]

def generate_azure_eco_permissions(eco_ro, subscription_id):
    with open("azure-base-def.json", 'r') as file:
        role_definition = json.load(file)
        # inject list of subscriptions
    inject_scope(subscription_id, role_definition)
        # inject Eco permissions
    role_definition = inject_permission(
            role_definition, eco_read_only, eco_full_access, eco_ro
        )
    with open("azure-eco-output.json", 'w') as file:
        file.write(json.dumps(role_definition, indent=4))
    return

################
# MAIN FUNCTION
################
def generate_azure_config(
    core_ro,
    products,
    eco_ro,
    elastigroup_ro,
    ocean_ro,
    netapp_storage,
    netapp_storage_ro,
    load_balancer,
    load_balancer_ro,
    dns,
    dns_ro,
    app_gateways,
    app_gateways_ro,
    application_security_groups,
    application_security_groups_ro,
    stateful,
    stateful_ro,
    subscription_id,
):

    if "Eco" in products:
        generate_azure_eco_permissions(eco_ro, subscription_id)

    if len(products) > 1:
        with open("azure-base-def.json", 'r') as file:
            role_definition = json.load(file)

        # inject list of subscriptions
        inject_scope(subscription_id, role_definition)

        # inject core permissions
        role_definition = inject_permission(
            role_definition, core_read_only, core_full_access, core_ro
        )

        if "Elastigroup" in products or "Ocean" in products:
            # inject Elastigroup permissions
            role_definition = inject_permission(
                role_definition, elastigroup_read_only, elastigroup_full_access, elastigroup_ro
            )
        if "Ocean" in products:
            # inject Ocean permissions
            role_definition = inject_permission(
                role_definition, ocean_read_only, ocean_full_access, ocean_ro
            )

        # inject NetApp Storage permissions
        role_definition = (
            inject_permission(
                role_definition,
                netapp_storage_read_only,
                netapp_storage_full_access,
                netapp_storage_ro,
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
                load_balancer_ro,
            )
            if load_balancer
            else role_definition
        )

        # inject DNS permissions
        role_definition = (
            inject_permission(role_definition, dns_read_only, dns_full_access, dns_ro)
            if dns
            else role_definition
        )

        # inject App Gateways permissions
        role_definition = (
            inject_permission(
                role_definition, app_gateways_read_only, app_gateways_full_access, app_gateways_ro
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
                application_security_groups_ro,
            )
            if application_security_groups
            else role_definition
        )

        # inject Stateful permissions
        role_definition = (
            inject_permission(
                role_definition, stateful_read_only, stateful_full_access, stateful_ro
            )
            if stateful
            else role_definition
        )

        with open("azure-non-eco-output.json", 'w') as file:
            file.write(json.dumps(role_definition, indent=4))

    return