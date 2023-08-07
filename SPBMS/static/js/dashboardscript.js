document.addEventListener("DOMContentLoaded", function() {
    // Get references to the card elements
    const totalBudgetCard = document.querySelector(".total-budget-card");
    const expensesCard = document.querySelector(".expenses-card");
    const savingsCard = document.querySelector(".savings-card");

    // Create chart for Total Budget
    const totalBudgetCtx = totalBudgetCard.querySelector("canvas").getContext("2d");
    new Chart(totalBudgetCtx, {
      type: "bar",
      data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
          {
            label: "Total Budget",
            data: [1200, 800, 1000, 900, 1100, 700],
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
    const expensesCtx = expensesCard.querySelector("canvas").getContext("2d");
    new Chart(expensesCtx, {
      type: "pie",
      data: {
        labels: ["Rent", "Groceries", "Transportation", "Entertainment"],
        datasets: [
          {
            label: "Expenses",
            data: [500, 200, 300, 100],
            backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0"],
          },
        ],
      },
    });

    // Create chart for Savings
    const savingsCtx = savingsCard.querySelector("canvas").getContext("2d");
    new Chart(savingsCtx, {
      type: "line",
      data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
          {
            label: "Savings",
            data: [100, 200, 150, 250, 180, 300],
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