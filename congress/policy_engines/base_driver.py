# Copyright (c) 2015 VMware, Inc. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from congress.dse import deepsix


class PolicyEngineDriver(deepsix.deepSix):
    """Driver for policy engines, analogous to DataSourceDriver."""

    def set_policy(self, policy):
        """Set the policy of this policy engine. POLICY is a datalog string."""
        return NotImplementedError

    def supported_language(self):
        """Return description of the language supported by this engine.

        A description is a list of permitted tables and a list of forbidden
        tables.  Eventually we may broaden the description.
        """
        return NotImplementedError
