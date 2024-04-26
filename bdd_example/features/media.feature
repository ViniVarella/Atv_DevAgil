# BDD = Exemplificar com testes casos de uso (features) do sistema/classes e assim colaborar com um time utilizando uma linguagem humana. 
# Pode ser lido por Stakeholder/PO/Scrum Master 

Feature: Calcular a média entre dois números
  Scenario: Somar os números e dividir o resultado por 2
    Given temos dois números inteiros: 10 e 32
    When somamos os dois números inteiros
    And dividimos a soma por 2
    Then o resultado deve ser 21