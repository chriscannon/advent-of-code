package common

import (
	"reflect"
	"testing"
)

func TestGetDigits(t *testing.T) {
	actual := GetDigits(123456, 6)
	expected := []int{1, 2, 3, 4, 5, 6}

	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("expected %v, but got %v", expected, actual)
	}
}
