document.addEventListener('DOMContentLoaded', function() {
  const addCategoryBtn = document.getElementById('add-category-btn');
  const categoryNameInput = document.getElementById('category-name');
  const categorySelect = document.getElementById('category');

  addCategoryBtn.addEventListener('click', function() {
    const newCategory = categoryNameInput.value.trim();

    // Check if the new category is not empty and not already in the select options
    if (newCategory && !categorySelect.querySelector(`[value="${newCategory}"]`)) {
      // Create a new option element and append it to the select element
      const option = document.createElement('option');
      option.value = newCategory;
      option.textContent = newCategory;
      categorySelect.appendChild(option);

      // Clear the input field after adding the category
      categoryNameInput.value = '';
    }
  });
});