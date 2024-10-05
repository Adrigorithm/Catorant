from generated import payment_pb2_grpc
from generated.payment_pb2 import PaymentReply, PaymentRequest


class Payment(payment_pb2_grpc.PaymentServicer):
    fake_bank = 1500

    def CreatePayment(self, request: PaymentRequest, context):
        isWithdrawal = request.amount < 0

        if isWithdrawal and self.fake_bank + request.amount < 0:
            return PaymentReply(False, "Insufficient funds")

        self.fake_bank += request.amount
        return PaymentReply(True)
