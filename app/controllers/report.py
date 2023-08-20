from app.repositories.models import db, Ingredient, OrderDetail, Order
from app.repositories.serializers import IngredientSerializer
from sqlalchemy import func, desc


class ReportController:
    session = db.session

    @classmethod
    def _get_top_ingredient(cls, serialized_ingredients: list):
        top_ingredient = serialized_ingredients[0]
        for ingredient in serialized_ingredients:
            if ingredient.get("requests") > top_ingredient.get("requests"):
                top_ingredient = ingredient
        return top_ingredient

    @classmethod
    def _get_top_month(cls, serialized_months: list):
        top_month = serialized_months[0]
        for month in serialized_months:
            if month.get("revenue") > top_month.get("revenue"):
                top_month = month
        return top_month

    @classmethod
    def _get_top_customer(cls, serialized_customers: list):
        sorted_customers = sorted(
            serialized_customers, key=lambda customer: customer.get("revenue"), reverse=True)
        return sorted_customers[:3]

    @classmethod
    def get_most_requested_ingredient(cls):
        try:
            response = cls.session.query(Ingredient, func.count(OrderDetail._id).label("requests")).join(
                OrderDetail).group_by(Ingredient._id).all()
            serialized_response = {"ingredients": [
                {"ingredient_id": row[0]._id, "ingredient_name": row[0].name, "requests": row[1]} for row in response]}
            top_ingredient = cls._get_top_ingredient(
                serialized_ingredients=serialized_response.get("ingredients"))
            serialized_response["top_ingredient"] = top_ingredient
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
            serialized_response = {"months": [
                {"year": row[0], "month": row[1], "revenue": round(row[2], 2)} for row in response]}
            top_month = cls._get_top_month(serialized_months=serialized_response.get("months"))
            serialized_response["top_month"] = top_month
            return serialized_response, None
        except Exception as e:
            return None, e

    @classmethod
    def get_revenue_by_customer(cls):
        try:
            response = cls.session.query(Order.client_name, func.sum(
                Order.total_price).label('revenue')).group_by(Order.client_name, Order.client_dni).all()
            serialized_response = {"customers": [
                {"client_name": row[0], "revenue": round(row[1], 2)} for row in response]}
            top_customers = cls._get_top_customer(
                serialized_customers=serialized_response.get("customers"))
            serialized_response["top_customers"] = top_customers
            return serialized_response, None
        except Exception as e:
            return None, e

    @classmethod
    def get_all(cls):
        try:
            ingredient_report = cls.get_most_requested_ingredient()[0]
            revenue_by_month = cls.get_revenue_by_month()[0]
            revenue_by_customer = cls.get_revenue_by_customer()[0]

            serialized_response = {"ingredient_report": ingredient_report,
                                   "revenue_by_month": revenue_by_month,
                                   "revenue_by_customer": revenue_by_customer}
            return serialized_response, None
        except Exception as e:
            return None, e
