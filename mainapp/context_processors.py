from basketapp.models import Basket


def basket(request):
    basket = []

    if request.user.is_active:
        basket = Basket.objects.filter(user=request.user)

    return {
        'basket': basket,
    }
