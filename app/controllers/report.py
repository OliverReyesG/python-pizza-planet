from app.repositories.models import db, Ingredient, OrderDetail, Order
from app.repositories.serializers import IngredientSerializer
from sqlalchemy import func, desc


class ReportController:
    session = db.session

    @classmethod
    def get_most_requested_ingredient(cls):
        try:
            response = cls.session.query(Ingredient, func.count(OrderDetail._id).label("requests")).join(
                OrderDetail).group_by(Ingredient._id).order_by(desc("requests")).all()
            serialized_response = [
                {"ingredient_id": row[0]._id, "ingredient_name": row[0].name, "requests": row[1]} for row in response]
            return serialized_response, None
        except Exception as e:
            return None, e

    @classmethod
    def get_revenue_by_month(cls):
        try:
            response = cls.session.query(
                func.extract('year', Order.date).label('year'),
                func.extract('month', Order.date).label('month'),
                func.sum(Order.total_price).label('record_count')
            ).group_by('year', 'month').all()
            serialized_response = [
                {"year": row[0], "month": row[1], "revenue": round(row[2], 2)} for row in response]
            return serialized_response, None
        except Exception as e:
            return None, e

    @classmethod
    def get_revenue_by_customer(cls):
        try:
            response = cls.session.query(Order.client_name, func.sum(
                Order.total_price).label('revenue')).group_by(Order.client_name, Order.client_dni).order_by(desc('revenue')).all()
            serialized_response = [
                {"client_name": row[0], "revenue": round(row[1], 2)} for row in response]
            return serialized_response, None
        except Exception as e:
            return None, e

    @classmethod
    def get_report(cls):
        try:
            ingredient_report = cls.get_most_requested_ingredient()[0]
            revenue_by_month = cls.get_revenue_by_month()[0]
            revenue_by_customer = cls.get_revenue_by_customer()[0]

            serialized_response = {"ingredient_report": ingredient_report,
                                   "revenue_by_month": revenue_by_month, "revenue_by_customer": revenue_by_customer}
            return serialized_response, None
        except Exception as e:
            return None, e
