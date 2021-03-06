# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkccc.endpoint import endpoint_data

class ModifySkillGroupOutboundNumbersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'ModifySkillGroupOutboundNumbers')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OperationType(self):
		return self.get_query_params().get('OperationType')

	def set_OperationType(self,OperationType):
		self.add_query_param('OperationType',OperationType)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_OutboundPhoneNumberIds(self):
		return self.get_query_params().get('OutboundPhoneNumberId')

	def set_OutboundPhoneNumberIds(self, OutboundPhoneNumberIds):
		for depth1 in range(len(OutboundPhoneNumberIds)):
			if OutboundPhoneNumberIds[depth1] is not None:
				self.add_query_param('OutboundPhoneNumberId.' + str(depth1 + 1) , OutboundPhoneNumberIds[depth1])

	def get_SkillGroupId(self):
		return self.get_query_params().get('SkillGroupId')

	def set_SkillGroupId(self,SkillGroupId):
		self.add_query_param('SkillGroupId',SkillGroupId)