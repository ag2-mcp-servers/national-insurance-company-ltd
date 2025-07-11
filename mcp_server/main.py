# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T15:14:34+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    CripcCertificatePostRequest,
    CripcCertificatePostResponse,
    CripcCertificatePostResponse1,
    CripcCertificatePostResponse2,
    CripcCertificatePostResponse3,
    CripcCertificatePostResponse4,
    CripcCertificatePostResponse5,
    CripcCertificatePostResponse6,
    CvipcCertificatePostRequest,
    CvipcCertificatePostResponse,
    CvipcCertificatePostResponse1,
    CvipcCertificatePostResponse2,
    CvipcCertificatePostResponse3,
    CvipcCertificatePostResponse4,
    CvipcCertificatePostResponse5,
    CvipcCertificatePostResponse6,
    EgipcCertificatePostRequest,
    EgipcCertificatePostResponse,
    EgipcCertificatePostResponse1,
    EgipcCertificatePostResponse2,
    EgipcCertificatePostResponse3,
    EgipcCertificatePostResponse4,
    EgipcCertificatePostResponse5,
    EgipcCertificatePostResponse6,
    GicerCertificatePostRequest,
    GicerCertificatePostResponse,
    GicerCertificatePostResponse1,
    GicerCertificatePostResponse2,
    GicerCertificatePostResponse3,
    GicerCertificatePostResponse4,
    GicerCertificatePostResponse5,
    GicerCertificatePostResponse6,
    HlipcCertificatePostRequest,
    HlipcCertificatePostResponse,
    HlipcCertificatePostResponse1,
    HlipcCertificatePostResponse2,
    HlipcCertificatePostResponse3,
    HlipcCertificatePostResponse4,
    HlipcCertificatePostResponse5,
    HlipcCertificatePostResponse6,
    HmipcCertificatePostRequest,
    HmipcCertificatePostResponse,
    HmipcCertificatePostResponse1,
    HmipcCertificatePostResponse2,
    HmipcCertificatePostResponse3,
    HmipcCertificatePostResponse4,
    HmipcCertificatePostResponse5,
    HmipcCertificatePostResponse6,
    MiipcCertificatePostRequest,
    MiipcCertificatePostResponse,
    MiipcCertificatePostResponse1,
    MiipcCertificatePostResponse2,
    MiipcCertificatePostResponse3,
    MiipcCertificatePostResponse4,
    MiipcCertificatePostResponse5,
    MiipcCertificatePostResponse6,
    MripcCertificatePostRequest,
    MripcCertificatePostResponse,
    MripcCertificatePostResponse1,
    MripcCertificatePostResponse2,
    MripcCertificatePostResponse3,
    MripcCertificatePostResponse4,
    MripcCertificatePostResponse5,
    MripcCertificatePostResponse6,
    PripcCertificatePostRequest,
    PripcCertificatePostResponse,
    PripcCertificatePostResponse1,
    PripcCertificatePostResponse2,
    PripcCertificatePostResponse3,
    PripcCertificatePostResponse4,
    PripcCertificatePostResponse5,
    PripcCertificatePostResponse6,
    TwipcCertificatePostRequest,
    TwipcCertificatePostResponse,
    TwipcCertificatePostResponse1,
    TwipcCertificatePostResponse2,
    TwipcCertificatePostResponse3,
    TwipcCertificatePostResponse4,
    TwipcCertificatePostResponse5,
    TwipcCertificatePostResponse6,
)

app = MCPProxy(
    description='APIs provided by National Insurance Company Ltd..',
    termsOfService='https://apisetu.gov.in/terms.php',
    title='National Insurance Company Ltd.',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/nationalinsurance/v3'}],
)


@app.post(
    '/cripc/certificate',
    description=""" API to verify Insurance Policy - Car. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def cripc(body: CripcCertificatePostRequest = None):
    """
    Insurance Policy - Car
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/cvipc/certificate',
    description=""" API to verify Insurance Policy - Commercial Vehicle. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def cvipc(body: CvipcCertificatePostRequest = None):
    """
    Insurance Policy - Commercial Vehicle
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/egipc/certificate',
    description=""" API to verify Insurance Policy - Engineering. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def egipc(body: EgipcCertificatePostRequest = None):
    """
    Insurance Policy - Engineering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/gicer/certificate',
    description=""" API to verify Insurance Policy - Group. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def gicer(body: GicerCertificatePostRequest = None):
    """
    Insurance Policy - Group
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/hlipc/certificate',
    description=""" API to verify Insurance Policy - Health. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def hlipc(body: HlipcCertificatePostRequest = None):
    """
    Insurance Policy - Health
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/hmipc/certificate',
    description=""" API to verify Insurance Policy - Home. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def hmipc(body: HmipcCertificatePostRequest = None):
    """
    Insurance Policy - Home
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/miipc/certificate',
    description=""" API to verify Insurance Policy - Miscellaneous. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def miipc(body: MiipcCertificatePostRequest = None):
    """
    Insurance Policy - Miscellaneous
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/mripc/certificate',
    description=""" API to verify Insurance Policy - Marine. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def mripc(body: MripcCertificatePostRequest = None):
    """
    Insurance Policy - Marine
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/pripc/certificate',
    description=""" API to verify Insurance Policy - Property. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def pripc(body: PripcCertificatePostRequest = None):
    """
    Insurance Policy - Property
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/twipc/certificate',
    description=""" API to verify Insurance Policy - Two Wheeler. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def twipc(body: TwipcCertificatePostRequest = None):
    """
    Insurance Policy - Two Wheeler
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
