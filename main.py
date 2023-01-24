import re
from InquirerPy import inquirer
from azure import generate_azure_config
from aws import generate_aws_config

################
# HELPER FUNCTIONS
################
def write_config(out, config):
    with open(out, "w") as f:
        f.write(config)


################
# MAIN FUNCTION
################
def main():
    cloud_providers = ["AWS", "Azure", "GCP"]
    product_options = ["Eco", "Elastigroup", "Ocean"]

    cloud = inquirer.select(
        message="Which cloud provider do you want to build permissions for?",
        choices=cloud_providers,
    ).execute()

    if cloud == "GCP":
        product_options.remove("Eco")

    core_ro = inquirer.confirm(
        message="Do you want the core Spot permissions to be read-only? If you select yes, and then select an option that enables write permissions, you may encounter errors and undefined behavior.",
        default=False,
    ).execute()

    products = inquirer.checkbox(
        message="Which Spot products do you want to use?",
        choices=product_options,
        validate=lambda result: len(result) >= 1,
        invalid_message="You must select at least 1 product",
        instruction="(select at least 1)",
    ).execute()

    if "Eco" in products:
        eco_ro = inquirer.confirm(
            message="Do you want to use Eco in read-only mode?",
            default=False,
        ).execute()
    else:
        eco_ro = False

    if "Elastigroup" in products:
        elastigroup_ro = inquirer.confirm(
            message="Do you want to use Elastigroup in read-only mode?",
            default=False,
        ).execute()
    else:
        elastigroup_ro = False

    if "Ocean" in products:
        ocean_ro = inquirer.confirm(
            message="Do you want to use Ocean in read-only mode?",
            default=False,
        ).execute()
    else:
        ocean_ro = False

    if cloud == "Azure":
        subscription_id = inquirer.text(
            message="Please enter the Azure Subscription ID you want to use.",
            validate=lambda result: re.fullmatch(
                r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
                result,
            ),
            invalid_message="You must enter exactly 1 Subscription ID in the format of 00000000-0000-0000-0000-000000000000",
        ).execute()

        netapp_storage = inquirer.confirm(
            message="Do you want to use NetApp Storage?", default=True
        ).execute()

        if netapp_storage:
            netapp_storage_ro = inquirer.confirm(
                message="Do you want to use NetApp Storage in read-only mode?",
                default=False,
            ).execute()
        else:
            netapp_storage_ro = False

        load_balancer = inquirer.confirm(
            message="Do you want to use load balancers?", default=True
        ).execute()

        if load_balancer:
            load_balancer_ro = inquirer.confirm(
                message="Do you want to use load balancers in read-only mode?",
                default=False,
            ).execute()
        else:
            load_balancer_ro = False

        dns = inquirer.confirm(
            message="Do you want to use DNS?", default=True
        ).execute()

        if dns:
            dns_ro = inquirer.confirm(
                message="Do you want to use DNS in read-only mode?", default=False
            ).execute()
        else:
            dns_ro = False

        app_gateways = inquirer.confirm(
            message="Do you want to use App Gateways?", default=True
        ).execute()

        if app_gateways:
            app_gateways_ro = inquirer.confirm(
                message="Do you want to use App Gateways in read-only mode?",
                default=False,
            ).execute()
        else:
            app_gateways_ro = False

        application_security_groups = inquirer.confirm(
            message="Do you want to use Application Security Groups?", default=True
        ).execute()

        if application_security_groups:
            application_security_groups_ro = inquirer.confirm(
                message="Do you want to use Application Security Groups in read-only mode?",
                default=False,
            ).execute()
        else:
            application_security_groups_ro = False

        stateful = inquirer.confirm(
            message="Do you want to use stateful instances?", default=True
        ).execute()

        if stateful:
            stateful_ro = inquirer.confirm(
                message="Do you want to use stateful instances in read-only mode?",
                default=False,
            ).execute()
        else:
            stateful_ro = False

        write_config(
            "out.json",
            generate_azure_config(
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
            ),
        )


if __name__ == "__main__":
    main()
