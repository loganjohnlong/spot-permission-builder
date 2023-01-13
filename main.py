import click
import re
import json
from azure import generate_azure_config

################
# GLOBAL VARIABLES
################
cloud_providers = ["AWS", "Azure", "GCP"]
product_options = ["Eco", "Elastigroup", "Ocean"]

################
# HELPER FUNCTIONS
################
def write_config(out, config):
    with open(out, "w") as f:
        f.write(config)
    click.echo(f"Config written to {out}")


################
# VALIDATION FUNCTIONS
################
def validate_cloud(ctx, param, value):
    if value not in cloud_providers:
        raise click.BadParameter(
            f"Invalid cloud provider. Valid options are: {cloud_providers}"
        )
    return value


def validate_products(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one product must be selected.")
    for product in value:
        if product not in product_options:
            raise click.BadParameter(
                f"Invalid product: {product}. Valid options are {product_options}"
            )
    return value


def validate_subscription_id(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one subscription ID must be provided.")
    # Regular expression pattern for a valid Azure Subscription ID
    pattern = re.compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
    )
    for subscription in value:
        if not pattern.match(subscription):
            raise click.BadParameter(
                "Subscription ID {value} is not valid. Please check the value and try again."
            )
    return value


################
# CLI OPTIONS
################
@click.command()
@click.option(
    "--cloud",
    type=click.Choice(cloud_providers, case_sensitive=False),
    callback=validate_cloud,
    help="Cloud provider to build permissions for",
)
@click.option(
    "--products",
    type=click.Choice(product_options, case_sensitive=False),
    multiple=True,
    callback=validate_products,
    help="Spot products that the customer wishes to use. Use this flag multiple times if specifying multiple products.",
)
@click.option(
    "--readonly",
    is_flag=True,
    default=False,
    help="If present, ALL permissions will be set to read-only.",
)
@click.option(
    "--netapp-storage",
    is_flag=True,
    default=False,
    help="Adds permissions for interfacing with NetApp Storage.",
)
@click.option(
    "--load-balancer",
    is_flag=True,
    default=False,
    help="Adds permissions for load balancers.",
)
@click.option("--dns", is_flag=True, default=False, help="Adds permissions for DNS.")
@click.option(
    "--app-gateways",
    is_flag=True,
    default=False,
    help="Adds permissions for App Gateways. (Azure only)",
)
@click.option(
    "--application-security-groups",
    is_flag=True,
    default=False,
    help="Adds permissions for Application Security Groups.",
)
@click.option(
    "--stateful",
    is_flag=True,
    default=False,
    help="Adds permissions for preserving state.",
)
@click.option(
    "--subscription-id",
    "subscription_ids",
    multiple=True,
    callback=validate_subscription_id,
    help="Azure Subscription ID. Use this flag multiple times to specify multiple IDs",
)
@click.option("--out", "outfile", required=True, type=click.Path(exists=False), help="Output file for the generated config")

################
# MAIN FUNCTION
################
def main(cloud, products, readonly, netapp_storage, load_balancer, dns, app_gateways, application_security_groups, stateful, subscription_ids, outfile):
    """Builds permissions for a given cloud provider and product(s)"""

    if cloud == "AWS":
        print("Performing AWS-specific tasks")
    elif cloud == "Azure":
        write_config(outfile, generate_azure_config(products, readonly, netapp_storage, load_balancer, dns, app_gateways, application_security_groups, stateful, subscription_ids))
    elif cloud == "GCP":
        print("Performing GCP-specific tasks")


if __name__ == "__main__":
    main()
