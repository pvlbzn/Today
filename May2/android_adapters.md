###Adapter

>An Adapter object acts as a bridge between an AdapterView and the underlying data for that view. The Adapter provides access to the data items. The Adapter is also responsible for making a View for each item in the data set.

```
	Data Source	<--->		Adapter	 	<--->		Visual Representation
```

Data can be a `Cursor` or an `ArrayList`. Visual Representation can be a `ListView`, `GridView`, `Spinner`, etc.

```
	ArrayList	<--->		ArrayAdapter	<--->		ListView
```

<br>

####View Recycling

The key idea is to save memory and gain a performance. If you have a 2^32 items long list, you don't need to upload all elements into the View. Instead you have to load only fixed amount of items in the View and recycle them as needed. This approach is used by Apple as well.

####ListView

```
1. ArrayList<T> al = new ArrayList<>(n);
2. 
3. // Get (or fake) the data.
4. 
5. ArrayAdapter<T> adapter = new ArrayAdapter<>(getActivity(), R.layout.list_item, al);
6. ListView lv = (ListView) [rootView].findViewById(R.id.some_list_view);
7. lv.setAdapter(adapter);
```

**5.**: `ArrayAdapter(Context context, int resource, List<T> objects)` where resource expected to be a TextView instance, at least I got an error while it was a FrameLayout. <br>
**6.**: Get an ID of `ListView`. <br>
**7.**: Set `ArrayAdapter` with `al` `ArrayList` on `ListView`. <br>

To be continued.
