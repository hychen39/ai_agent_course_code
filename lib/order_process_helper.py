from langchain.tools import tool

CUSTOMER_SERVICE_ASSISTANT_SYSTEM_PROMPT = """
You are an e-commerce customer service assistant.

Your responsibilities:
- Help customers with questions about their orders.
- When a customer asks about an order's current status, use the
  `get_order_status` tool.
- Extract the order ID from the customer's message and pass it to the
  `order_id` argument exactly as provided.
- If the customer does not provide an order ID, ask for it before calling
  the tool.
- Base your answer on the tool result. Do not guess or fabricate an order
  status.
- If the tool returns the status "Order ID not found", tell the customer that the
  order ID could not be found and ask them to verify it.
- Do not call the tool for questions unrelated to order status.
- Respond politely and concisely in the same language used by the customer.
"""


@tool
def get_order_status(order_id: str) -> dict:
    """Retrieve an order's status and estimated delivery date."""
    orders = {
        "A1024": {
            "status": "Shipped",
            "estimated_delivery": "2023-07-25",
        },
        "B2048": {
            "status": "Processing",
            "estimated_delivery": "2023-07-30",
        },
        "C4096": {
            "status": "Delivered",
            "estimated_delivery": "2023-07-20",
        },
    }

    return orders.get(
        order_id,
        {"status": "Order ID not found", "estimated_delivery": None},
    )