## Javadoc

Javadoc is a tool used for generating code documentation in HTML format out of Java source code. Javadoc starts with `/**` comment tag and ends with `*/` closing tag. It can be a plain text and a text with tags.

Just be aware of a bloat. Too much writting for a 3 lines method is not good idea. Self documenting code is a best code.

### Tags

```
@author             Describes an author                 class/interface
@version            Provides software version           class/interface
@since              Describes when this                 class/interface
                    functionality has appeared
@see                Provides a link to other doc        whatever
                    element
@param              Describes a method parameter        method
@return             Describes the return value          method
@exception          Describes an exception that         method
                    may be thrown
@throws             -=-                                 method
@deprecated         Describes an outdated method        everythins
{@inheritDoc}       Copies the description from         method
                    the overriden method
{@link}             Link to other symbol                everything
{@value}            Return the value of a static        static field
                    field
{@code}             Formats literal text in the         everythins
                    code font       
{@literal}          Denotes literal text.               everything
```

```
/**
 * Simple calculator operation.
 * @author <a href="mailto:me@my.com">Me</a>
 * @version 1.0
 */
public interface Operation {
    /**
     * Perform a single calculation.
     * @param operand the operand to use for calculation.
     */
    public void calculate(double operand);

    /**
     * Get the current result.
     * @return the current result. If no calculations were
     *         performed the result is undefined.
     */
    public double getResult();
}
```
