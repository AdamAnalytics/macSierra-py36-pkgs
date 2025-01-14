Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Key Vault Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

For the older Azure Service Management (ASM) libraries, see
`azure-servicemanagement-legacy <https://pypi.python.org/pypi/azure-servicemanagement-legacy>`__ library.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Usage
=====

For code examples, see `Key Vault
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-keyvault.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============
0.3.6 (2017-08-16)
++++++++++++++++++

* Updated KeyVaultClient to accept both KeyVaultAuthentication and azure.common.credentials instances for authentication

0.3.5 (2017-06-23)
++++++++++++++++++

* Fix: https://github.com/Azure/azure-sdk-for-python/issues/1159
* KeyVaultId refactoring
  - adding object specific id classes to make usage more uniform with other key vault SDKs
  - added storage account id and storage sas definition id parsing and formatting

0.3.4 (2017-06-07)
++++++++++++++++++

* Adding Preview Features
  - Managed Storage Account keys for managing storage credentials and provisioning SAS tokens
  - Key Vault "Soft Delete" allowing for recovery of deleted keys, secrets and certificates
  - Secret Backup and Restore for secret recovery and migration

0.3.3 (2017-05-10)
++++++++++++++++++

* Reverting to 0.3.0, since behavior of 0.3.2 is not satisfaying either.

0.3.2 (2017-05-09)
++++++++++++++++++

* Fix critical regression on 0.3.1 (#1157)
* Now the client respects 'REQUESTS_CA_BUNDLE' and 'CURL_CA_BUNDLE'

0.3.1 (2017-05-09)
++++++++++++++++++

* Support for REQUESTS_CA_BUNDLE (#1154)

0.3.0 (2017-05-08)
++++++++++++++++++

* Moving KeyVaultClient class to the azure.keyvault namespace
* Moving model classes to the azure.keyvault.models namespace
* Deprecating 'generated' namespaces azure.keyvault.generated and azure.keyvault.generated.models
* Exposed KeyVaultId class through azure.keyvault namespace
* Moving identifier parsing methods to static methods on KeyVaultId class
* Removing convenience overridden methods from KeyVaultClient
  - update_key(self, key_identifier, ...
  - get_key(self, key_identifier, ...
  - encrypt(self, key_identifier, ...
  - decrypt(self, key_identifier, ...
  - sign(self, key_identifier, ...
  - verify(self, key_identifier, ...
  - wrap_key(self, key_identifier, ...
  - unwrap_key(self, key_identifier, ...
  - update_secret(self, secret_identifer, ...
  - get_secret(self, secret_identifer, ...
  - get_certificate(self, certificate_identifier, ...

0.2.0 (2017-04-19)
++++++++++++++++++

**Bugfixes**

- Fix possible deserialization error, but updating from list<enumtype> to list<str> when applicable

**Notes**

- This wheel package is now built with the azure wheel extension

0.1.0 (2016-12-29)
++++++++++++++++++

* Initial Release


