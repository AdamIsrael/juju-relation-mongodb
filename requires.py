# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class MongoDBRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:mongodb}-relation-joined')
    def joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')

    @hook('{requires:mongodb}-relation-changed')
    def changed(self):
        conv = self.conversation()
        if self.mongodbs():
            conv.set_state('{relation_name}.ready')
        else:
            conv.remove_state('{relation_name}.ready')

    @hook('{requires:mongodb}-relation-departed')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.ready')
        conv.remove_state('{relation_name}.joined')

    def mongodbs(self):
        mongodbs = []
        for conv in self.conversations():
            port = conv.get_remote('port')
            host = conv.get_remote('host') or conv.get_remote(
                'private-address')
            if port:
                mongodbs.append({
                    'host': host,
                    'port': port
                })
        return mongodbs
