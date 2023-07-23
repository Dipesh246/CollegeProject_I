function calculateBudget() {
    const monthlyIncome = parseFloat(document.getElementById('monthly-income').value);
    const housingExpenses = parseFloat(document.getElementById('housing-expenses').value);
    const foodExpenses = parseFloat(document.getElementById('food-expenses').value);
    const entertainmentExpenses = parseFloat(document.getElementById('entertainment-expenses').value);

    const totalExpenses = housingExpenses + foodExpenses + entertainmentExpenses;
    const remainingBudget = monthlyIncome - totalExpenses;

    alert(`Your total expenses: $${totalExpenses.toFixed(2)}`);
    alert(`Your remaining budget: $${remainingBudget.toFixed(2)}`);
  }