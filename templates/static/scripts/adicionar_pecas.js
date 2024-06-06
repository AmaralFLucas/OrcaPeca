var listItens = []

document.querySelector(".btn-add").addEventListener("click", function () {
  var tbody = document.getElementById("itemsBody");

  var newRow = document.createElement("tr");

  var pecaCell = document.createElement("td");
  var quantidadeCell = document.createElement("td");

  var pecaValue = document.getElementById("peca").value;
  var quantidadeValue = document.getElementById("quantidade").value;

  pecaCell.textContent = pecaValue;
  quantidadeCell.textContent = quantidadeValue;

  newRow.appendChild(pecaCell);
  newRow.appendChild(quantidadeCell);

  tbody.appendChild(newRow);

  document.getElementById("peca");

  listItens.push({"peca":pecaValue, "quantidade":quantidadeValue})
  document.getElementById("itens").value = JSON.stringify(listItens);

  document.getElementById("peca").value = '';
  document.getElementById("quantidade").value = '';

  console.log(JSON.stringify(listItens));
});
