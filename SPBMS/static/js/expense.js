
  document.addEventListener('DOMContentLoaded', function() {
    const budgetNameInput = document.getElementById('budget-name');
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');

    budgetNameInput.addEventListener('input', function () {
      if (budgetNameInput.value.toLowerCase() === 'monthly budget') {
        const currentDate = new Date().toISOString().split('T')[0];
        startDateInput.value = currentDate;
        const nextMonthDate = new Date();
        nextMonthDate.setMonth(nextMonthDate.getMonth() + 1);
        endDateInput.value = nextMonthDate.toISOString().split('T')[0];
      }
    });

    startDateInput.addEventListener('input', function () {
      const startDate = new Date(startDateInput.value);
      const endDate = new Date(startDate);
      endDate.setMonth(endDate.getMonth() + 1);
      endDateInput.value = endDate.toISOString().split('T')[0];
    });
  });