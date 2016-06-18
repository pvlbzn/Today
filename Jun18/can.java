@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface Test {
   String info() default "";
}


class Annotated {

   @Test(info = "TestInfo")
   public void foo(String myParam) {
      System.out.println("This is " + myParam);
   }

}


class TestAnnotationParser {

   public void parse(Class> clazz) throws Exception {
      Method[] methods = clazz.getMethods();
      
      for (Method method : methods) {
         if (method.isAnnotationPresent(Test.class)) {
            Test test = method.getAnnotation(Test.class);
            String info = test.info();
            if ("TestInfo".equals(info)) {
                System.out.println("info is awesome!");
                method.invoke(
                   Annotated.class.newInstance(),
                   info
                );
            }
         }
      }
   }

}


public class Demo {

   public static void main(String[] args) throws Exception {
      TestAnnotationParser parser = new TestAnnotationParser();
      parser.parse(Annotated.class);
   }

}
