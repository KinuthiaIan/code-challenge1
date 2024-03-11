function solution(A, D) {
    let balance = 0;
    let monthlyFee = 5;
    let paymentsByCard = 0;
    let paymentsByCardThisMonth = 0;
    let monthlyIncome = 0;
    let monthlyExpenditure = 0;
    let currentMonth = 0;
  
    for (let i = 0; i < A.length; i++) {
      const amount = A[i];
      const date = new Date(D[i]);
  
      balance += amount;
  
      if (amount > 0) {
        monthlyIncome += amount;
      } else {
        monthlyExpenditure -= amount;
        paymentsByCard += amount;
        paymentsByCardThisMonth += amount;
      }
  
      if (date.getMonth() !== currentMonth) {
        if (paymentsByCardThisMonth < 100 || i === A.length - 1) {
          balance -= monthlyFee;
        }
  
        currentMonth = date.getMonth();
        monthlyIncome = 0;
        monthlyExpenditure = 0;
        paymentsByCardThisMonth = 0;
      }
    }
  
    return balance;
  }