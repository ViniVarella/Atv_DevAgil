from behave import given, step, then

@given('Temos dois números inteiros: {num1:d} e {num2:d}')
def step_impl(ctx, num1, num2):
  ctx.num1 = num1
  ctx.num2 = num2

@step('Somamos esses dois números')
def step_impl(ctx):
  ctx.soma = ctx.num1 + ctx.num2

@step('Dividimos o resultado por 2')
def step_impl(ctx):
  ctx.resultado = ctx.soma / 2

@then('O resultado será: {resultado:d}')
def step_impl(ctx, resultado):
  assert ctx.resultado == resultado, f"Resultado Incorreto. Esperado {resultado}. Obtido: {ctx.resultado}"

