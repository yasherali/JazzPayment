from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class JazzCashReturnView(View):
    def post(self, request, *args, **kwargs):
        # JazzCash sends payment details in the request
        transaction_status = request.POST.get('pp_ResponseCode')  # Response code
        transaction_message = request.POST.get('pp_ResponseMessage')  # Response message
        order_id = request.POST.get('pp_TxnRefNo')  # Order reference

        # Validate the transaction (response codes vary based on success/failure)
        if transaction_status == "000":  # 000 usually indicates success
            return HttpResponse("Payment Successful")
        else:
            return HttpResponse(f"Payment Failed: {transaction_message}")

    def get(self, request, *args, **kwargs):
        return HttpResponse("JazzCash Return URL")