__all__ = ['tk']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['b', 'TKK', 'tk'])
@Js
def PyJsHoisted_b_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c', 'd'])
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<(var.get('b').get('length')-Js(2.0))):
        try:
            var.put('c', var.get('b').callprop('charAt', (var.get('d')+Js(2.0))))
            var.put('c', ((var.get('c').callprop('charCodeAt', Js(0.0))-Js(87.0)) if (Js('a')<=var.get('c')) else var.get('Number')(var.get('c'))))
            var.put('c', (PyJsBshift(var.get('a'),var.get('c')) if (Js('+')==var.get('b').callprop('charAt', (var.get('d')+Js(1.0)))) else (var.get('a')<<var.get('c'))))
            var.put('a', (((var.get('a')+var.get('c'))&Js(4294967295.0)) if (Js('+')==var.get('b').callprop('charAt', var.get('d'))) else (var.get('a')^var.get('c'))))
        finally:
                var.put('d', Js(3.0), '+')
    return var.get('a')
PyJsHoisted_b_.func_name = 'b'
var.put('b', PyJsHoisted_b_)
@Js
def PyJsHoisted_tk_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['h', 'c', 'f', 'e', 'g', 'd', 'a'])
    #for JS loop
    var.put('e', var.get('TKK').callprop('split', Js('.')))
    var.put('h', (var.get('Number')(var.get('e').get('0')) or Js(0.0)))
    var.put('g', Js([]))
    var.put('d', Js(0.0))
    var.put('f', Js(0.0))
    while (var.get('f')<var.get('a').get('length')):
        try:
            var.put('c', var.get('a').callprop('charCodeAt', var.get('f')))
            def PyJs_LONG_3_(var=var):
                def PyJs_LONG_2_(var=var):
                    def PyJs_LONG_1_(var=var):
                        return PyJsComma(PyJsComma(var.put('c', ((Js(65536.0)+((var.get('c')&Js(1023.0))<<Js(10.0)))+(var.get('a').callprop('charCodeAt', var.put('f',Js(var.get('f').to_number())+Js(1)))&Js(1023.0)))),var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), ((var.get('c')>>Js(18.0))|Js(240.0)))),var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), (((var.get('c')>>Js(12.0))&Js(63.0))|Js(128.0))))
                    return PyJsComma((PyJs_LONG_1_() if (((Js(55296.0)==(var.get('c')&Js(64512.0))) and ((var.get('f')+Js(1.0))<var.get('a').get('length'))) and (Js(56320.0)==(var.get('a').callprop('charCodeAt', (var.get('f')+Js(1.0)))&Js(64512.0)))) else var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), ((var.get('c')>>Js(12.0))|Js(224.0)))),var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), (((var.get('c')>>Js(6.0))&Js(63.0))|Js(128.0))))
                return (var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), var.get('c')) if (Js(128.0)>var.get('c')) else PyJsComma((var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), ((var.get('c')>>Js(6.0))|Js(192.0))) if (Js(2048.0)>var.get('c')) else PyJs_LONG_2_()),var.get('g').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), ((var.get('c')&Js(63.0))|Js(128.0)))))
            PyJs_LONG_3_()
        finally:
                (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
    var.put('a', var.get('h'))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('g').get('length')):
        try:
            PyJsComma(var.put('a', var.get('g').get(var.get('d')), '+'),var.put('a', var.get('b')(var.get('a'), Js('+-a^+6'))))
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.put('a', var.get('b')(var.get('a'), Js('+-3^+b+-f')))
    var.put('a', (var.get('Number')(var.get('e').get('1')) or Js(0.0)), '^')
    ((Js(0.0)>var.get('a')) and var.put('a', ((var.get('a')&Js(2147483647.0))+Js(2147483648.0))))
    var.put('a', Js(1000000.0), '%')
    return ((var.get('a').callprop('toString')+Js('.'))+(var.get('a')^var.get('h')))
PyJsHoisted_tk_.func_name = 'tk'
var.put('tk', PyJsHoisted_tk_)
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('a', Js(561666268.0))
    var.put('b', Js(1526272306.0))
    return ((Js(406398.0)+Js('.'))+(var.get('a')+var.get('b')))
PyJs_anonymous_0_._set_name('anonymous')
var.put('TKK', PyJs_anonymous_0_())
pass
pass
pass


# Add lib to the module scope
tk = var.to_python()