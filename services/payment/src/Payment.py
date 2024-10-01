from generated import payment_pb2_grpc
from generated.payment_pb2 import PaymentReply


class Payment(payment_pb2_grpc.PaymentServicer):
    def CreatePayment(self, request, context):
        return PaymentReply()
