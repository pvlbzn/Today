###Fragments

Fragment represents a behavior or a portion of UI in an activity. You can think of a fragment as a modular section of an activity, which has its own lifecycle, receives its own input events, and which you can add or remove while the activity is running.

This is what [documentation](http://developer.android.com/guide/components/fragments.html) states about fragments. I tried to build an app using activities and fragments. Android comunity (kind of community, because 'Android community' is something non-existend or I can't find it) has two opinions:

a. Use only Activities
b. Use one Activity and all Fragments

I have no proper experience, this is why this paper is in "Today I Learned", but I guess best option is a third option: use both. Use a **right tool for the job**.

Main benefits of Fragments, in my opinion:

- Modularity
- Clear project structure
- Flexibility

Kind of downside that Fragments are harder to understand. However I don't think that beneficial difficulty can be called as a 'downside'.

<br>

####Communication

Communication between Fragments and to Fragment must be done through parent Activity via callbacks implementing some interface.

<br>

####Life-cycle

Fragments have their own [life-cycle](http://developer.android.com/images/fragment_lifecycle.png).

<br>

####Adding a Fragment

- Declare inside the activity's layout file
- Programmatically add the fragment to an existing ViewGroup

Due to dynamic nature of fragments, it is really natural to add them, well, dynamically.

<br>

####ViewSomething

There are View and ViewGroup:

**View**: contains stuff as `TextView`, `Button`, etc.
**ViewGroup**: contains groups such as `FrameLayout`, `LinearLayout`.

<br>

####FragmentManager

Manipulations with fragments are performed using a `FragmentManager`.


<br>

This is a brief intro into Fragments and Android in general. There are still much more questions than answers.
