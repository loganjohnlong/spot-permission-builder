import yaml

################
# GLOBAL VARIABLES
################

## NOTE: The '*full_access' lists only contain the additional permissions needed to go from read only to full access. They cannot be used as-is.
core_read_only = [
    "iam.serviceAccounts.get",
    "iam.serviceAccounts.list",
    "iam.serviceAccounts.update",
    "monitoring.metricDescriptors.list",
    "monitoring.timeSeries.list",
    "servicemanagement.services.check",
    "servicemanagement.services.report",
]

core_full_access = [
]

elastigroup_read_only = [
    "compute.backendServices.get",
    "compute.backendServices.list",
    "compute.diskTypes.get",
    "compute.diskTypes.list",
    "compute.disks.get",
    "compute.disks.list",
    "compute.disks.use",
    "compute.globalOperations.get",
    "compute.globalOperations.list",
    "compute.healthChecks.useReadOnly",
    "compute.httpHealthChecks.useReadOnly",
    "compute.httpsHealthChecks.useReadOnly",
    "compute.images.get",
    "compute.images.list",
    "compute.images.useReadOnly",
    "compute.instanceGroupManagers.get",
    "compute.instanceGroups.get",
    "compute.instanceGroups.list",
    "compute.instanceGroups.use",
    "compute.instanceTemplates.get",
    "compute.instances.get",
    "compute.instances.list",
    "compute.instances.listReferrers",
    "compute.instances.use",
    "compute.machineTypes.get",
    "compute.machineTypes.list",
    "compute.networks.get",
    "compute.networks.list",
    "compute.projects.get",
    "compute.regionBackendServices.get",
    "compute.regionBackendServices.list",
    "compute.regionOperations.get",
    "compute.regionOperations.list",
    "compute.snapshots.get",
    "compute.snapshots.list",
    "compute.subnetworks.use",
    "compute.subnetworks.useExternalIp",
    "compute.targetPools.addInstance",
    "compute.targetPools.get",
    "compute.targetPools.list",
    "compute.targetPools.removeInstance",
    "compute.zoneOperations.get",
    "compute.zoneOperations.list",
    "compute.zones.list",
]

elastigroup_full_access = [
    "compute.addresses.create",
    "compute.addresses.createInternal",
    "compute.addresses.delete",
    "compute.addresses.get",
    "compute.addresses.list",
    "compute.addresses.setLabels",
    "compute.addresses.useInternal",
    "compute.backendServices.update",
    "compute.disks.create",
    "compute.disks.createSnapshot",
    "compute.disks.delete",
    "compute.disks.update",
    "compute.images.create",
    "compute.images.delete",
    "compute.instanceGroups.create",
    "compute.instanceGroups.update",
    "compute.instances.attachDisk",
    "compute.instances.create",
    "compute.instances.delete",
    "compute.instances.setLabels",
    "compute.instances.setMetadata",
    "compute.instances.setServiceAccount",
    "compute.instances.setTags",
    "compute.instances.start",
    "compute.instances.stop",
    "compute.instances.update",
    "compute.instances.setDiskAutoDelete",
    "compute.regionBackendServices.update",
    "compute.snapshots.create",
    "compute.snapshots.delete",
]

ocean_read_only = [
    "container.clusterRoles.bind",
    "container.clusters.get",
    "container.clusters.list",
    "container.operations.get",
    "container.operations.list",
]

ocean_full_access = [
    "container.clusterRoleBindings.create",
    "container.clusters.update",
]

################
# HELPER FUNCTIONS
################
def inject_permission(role_def, permissions_ro, permissions_full, readonly):
    if readonly:
        role_def["includedPermissions"] += permissions_ro
    else:
        role_def["includedPermissions"] += (
            permissions_ro + permissions_full
        )
    return role_def


################
# MAIN FUNCTION
################
def generate_gcp_config(
    core_ro,
    products,
    elastigroup_ro,
    ocean_ro
):

    with open("gcp-base-def.yaml", 'r') as file:
        role_definition = yaml.safe_load(file)

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

    return yaml.dump(role_definition)
