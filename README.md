# README Prod Alarm Forwarder

A Cloudformation template targeting to deploy the AWS serverless backend to interact with ServiceNow for user provisionning 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Installation

**Version beta**: the template currently deploy one API gateway with a post method, two lambda functions, one in nodejs to authorize using the api only with the right credentials, one in python bundled with the pysnow library to process and update the request.

Launch the Cloudformation Stack.

## Usage

Output: 

## Support

Please [open an issue](https://confluence.gemalto.com/pages/viewpage.action?pageId=278568171) for support.

