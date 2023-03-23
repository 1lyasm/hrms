#include <cassert>
#include "example.h"

struct TestExample {
	static void test_example_func() {
		Example example_obj;
		assert(example_obj.example_func() == 0);
	}
};

int main() {
	TestExample::test_example_func();
	return 0;
}

