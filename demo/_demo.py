from kutty import Code, html

def Demo(code, target_var):
    env = {}
    exec(code, env)
    component = env[target_var]

    demo = html.div(class_="demo")
    d1 = html.div(class_="demo-preview")
    d1 << component
    demo << d1

    d2 = html.div(class_="demo-code")
    d2 << Code(code)
    demo << d2

    return demo
