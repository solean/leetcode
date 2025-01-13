package deque

type Deque[T any] struct {
	items []T
}

func New[T any]() *Deque[T] {
	return &Deque[T]{
		items: make([]T, 0),
	}
}

func (d *Deque[T]) Append(value T) {
	d.items = append(d.items, value)
}

func (d *Deque[T]) PopLeft() T {
	if len(d.items) == 0 {
		panic("Deque is empty")
	}
	value := d.items[0]
	d.items = d.items[1:]
	return value
}

func (d *Deque[T]) Size() int {
	return len(d.items)
}

func (d *Deque[T]) IsEmpty() bool {
	return len(d.items) == 0
}
