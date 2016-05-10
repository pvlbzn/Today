####Template

Go has two packages with the same API: `text/template`, `html/template`. HTML output safe againts code injection and should be used instead of `text/template` whenever the output is HTML.

`Actions` - data evaluations or control structures are delimited by `{{` and `}}`.

```
type Inventory struct {
    Material    string
    Count       uint
}

sweaters := Inventory{"wool", 17}
tmpl, err := template.New("test").Parse("{{.Cound}} items are made of {{.Material}}")
if err != nil {
    panic(err)
}
err = tmpl.Execute(os.Stdout, sweaters)
if err != nil {
    panic(err)
}
```

<br>

####Trim

Trim left `{{-`, trim right `-}}`.

```
"{{23 -}} < {{- 45}}"
```

Will generate `"23<45"`.

<br>

####Pipe and dot

Pipe is similar to pipeline in Unix-like OS: `ls -a | grep .go`. The dot is used to refer to the current pipeline. This is similar to cursor used with DB.

####Actions

```
{{/* comment */}}

{{pipeline}}

{{if pipeline}} T1 {{end}}
If the value of the pipeline is empty, no output is generated,
otherwise T1 is executed.

{{if pipeline}} T1 {{else}} T0 {{end}}

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}

{{range pipeline}} T1 {{end}}
Works with an array, slice, map or channel.

{{template "name" pipeline}}
The template with the specified name is executed with dot set
to the value of th pipeline.

{{template "name"}}
The same, but with nil data.

{{block "name" pipeline}} T1 {{end}}

{{with pipeline}} T1 {{end}}
If the value of the pipeline is empty, no output is generated,
otherwise, dot is set to the value of the pipeline and T1 is executed.

{{with pipeline}} T1 {{else}} T0 {{end}}
Of the value of the pipline is empty, dot is unaffected and T0 is executed.
```

<br>

####Variable

```
$var := pipeline

range $k, $v := pipeline
```

<br>

####Examples

```
{{"\"output\""}}        A string constant

{{`"output"`}}          A raw string constant

{{printf "%q" "output"}}        A function call

{{"output" | printf "%q"}}      A function call whose final arg
                                comes from the prev command.

{{printf "%q" (print "out" "put")}}     A parenthesized arg.

{{"put" | printf "%s" | printf "%q"}}   A longer chain.

{{with "output"}}{{printf "%q" .}}{{end}}   With action using dot.

{{with $x := "output" | printf "%q" $x}}{{end}}     With action that uses the var in
                                                    another action.
```
