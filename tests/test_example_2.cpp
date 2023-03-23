#include <cassert>
#include "example_2.h"

struct TestExample_2 {
	static void test_example_2_func() {
		Example_2 example_obj;
		assert(example_obj.example_2_func() == 1);
	}
};

int main() {
	TestExample_2::test_example_2_func();
	return 0;
}

