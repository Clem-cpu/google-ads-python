# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.services import user_data_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_user__data__service__pb2


class UserDataServiceStub(object):
  """Proto file describing the UserDataService.

  Service to manage user data uploads.
  Accessible to whitelisted customers only.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadUserData = channel.unary_unary(
        '/google.ads.googleads.v3.services.UserDataService/UploadUserData',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_user__data__service__pb2.UploadUserDataRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_user__data__service__pb2.UploadUserDataResponse.FromString,
        )


class UserDataServiceServicer(object):
  """Proto file describing the UserDataService.

  Service to manage user data uploads.
  Accessible to whitelisted customers only.
  """

  def UploadUserData(self, request, context):
    """Uploads the given user data.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserDataServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadUserData': grpc.unary_unary_rpc_method_handler(
          servicer.UploadUserData,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_user__data__service__pb2.UploadUserDataRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_user__data__service__pb2.UploadUserDataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.UserDataService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))