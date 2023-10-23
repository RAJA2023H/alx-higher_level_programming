#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints python list
 *
 * @p: PyObject
 * Return: no return
 */

void print_python_list_info(PyObject *p) 
{
	const char *item_type_name;
	long int size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	rintf("[*] Allocated = %li\n", list->allocated);

	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(list, i);
		item_type_name = Py_TYPE(item)->tp_name;
		printf("Element %i: %s\n", i, item_type_name);
	}

}
