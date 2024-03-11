from datetime import datetime

def solution(A, D, N):
    # Initialize variables
    balance = 0
    monthly_fee = 5
    payments_by_card = 0
    payments_by_card_this_month = 0
    monthly_income = 0
    monthly_expenditure = 0
    current_month = 0
    # Process transactions
    for i in range(N):
        # Get transaction amount and date
        amount = A[i]
        date = datetime.strptime(D[i], '%Y-%m-%d')
        # Update balance
        balance += amount
        # Update monthly income and expenditure
        if amount > 0:
            monthly_income += amount
        else:
            monthly_expenditure -= amount
        # Update payments by card
        if amount < 0:
            payments_by_card += amount
            payments_by_card_this_month += amount
        # Check if it's a new month
        if date.month != current_month:
            # Check if the fee should be paid
            if payments_by_card_this_month < 100 or i == N-1:
                balance -= monthly_fee
            # Reset monthly variables
            current_month = date.month
            monthly_income = 0
            monthly_expenditure = 0
            payments_by_card_this_month = 0
    return balance