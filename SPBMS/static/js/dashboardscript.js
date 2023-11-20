document.addEventListener("DOMContentLoaded", function() {
  const budgetsData = JSON.parse(document.querySelector(".total-budget-card").getAttribute("data-budgets"));
  const expensesData = JSON.parse(document.querySelector(".expenses-card").getAttribute("data-expenses"));
  const savingsData = JSON.parse(document.querySelector(".savings-card").getAttribute("data-savings"));
  
  
  // Create chart for Total Budget
  const totalBudgetCard = document.querySelector(".total-budget-card");
  const totalBudgetCtx = totalBudgetCard.querySelector("canvas").getContext("2d");
  new Chart(totalBudgetCtx, {
    type: "bar",
    data: {
      labels: budgetsData.map(budget => budget.name),
      datasets: [
        {
          label: "Total Budget",
          data: budgetsData.map(budget => budget.total_budget),
          backgroundColor: "#36a2eb",
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  // Create chart for Expenses
  const expensesCard = document.querySelector(".expenses-card");
  const expensesCtx = expensesCard.querySelector("canvas").getContext("2d");
  new Chart(expensesCtx, {
    type: "pie",
    data: {
      labels: expensesData.map(item => item.category),
      datasets: [
        {
          label: "Expenses",
          data: expensesData.map(item => item.total_spendings),
          backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0"],
        },
      ],
    },
  });

  // Create chart for Savings
  const savingsCard = document.querySelector(".savings-card");
  const savingsCtx = savingsCard.querySelector("canvas").getContext("2d");
  new Chart(savingsCtx, {
    type: "line",
    data: {
      labels: expensesData.map(item => item.category),
      datasets: [
        {
          label: "Savings",
          data: expensesData.map(item => item.total_savings),
          borderColor: "#ff6384",
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});
