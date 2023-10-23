#include <stdio.h>
#include <stddef.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

struct _object {
	PyObject_VAR_HEAD
};

struct _listobject {
	PyObject_VAR_HEAD
	PyObject **ob_item;
	Py_ssize_t allocated;
};

typedef struct _object PyObject;
typedef struct _listobject PyListObject;

void print_python_list_info(PyObject *p)
{
	PyListObject *obj = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = obj->ob_item[i];
		printf("Element %li: %s\n", i, item->ob_type->tp_name);
	}
}
