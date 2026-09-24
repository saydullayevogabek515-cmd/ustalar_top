from .models import Order
from .serializers import OrderSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Order.objects.none()

        if user.role == "CUSTOMER":
            return Order.objects.filter(customer=user)

        if user.role == "MASTER":
            return Order.objects.filter(master__user=user)

        return Order.objects.none()

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.Status.PENDING:
            return Response(
                {"detail": "Bu orderni accept qilib bo'lmaydi."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.ACCEPTED
        order.save(update_fields=["status", "updated_at"])

        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.Status.PENDING:
            return Response(
                {"detail": "Bu orderni reject qilib bo'lmaydi."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.REJECTED
        order.save(update_fields=["status", "updated_at"])

        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["post"])
    def start(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.Status.ACCEPTED:
            return Response(
                {"detail": "Faqat ACCEPTED orderni boshlash mumkin."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.IN_PROGRESS
        order.save(update_fields=["status", "updated_at"])

        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.Status.IN_PROGRESS:
            return Response(
                {"detail": "Faqat IN_PROGRESS orderni tugatish mumkin."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.COMPLETED
        order.save(update_fields=["status", "updated_at"])

        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        order = self.get_object()

        if order.status not in [
            Order.Status.PENDING,
            Order.Status.ACCEPTED,
            Order.Status.IN_PROGRESS,
        ]:
            return Response(
                {"detail": "Bu orderni cancel qilib bo'lmaydi."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.CANCELLED
        order.save(update_fields=["status", "updated_at"])

        return Response(OrderSerializer(order).data)