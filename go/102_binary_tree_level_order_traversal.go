package main

import (
	"github.com/solean/leetcode/deque"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	levels := [][]int{}

	d := deque.New[*TreeNode]()
	d.Append(root)

	for !d.IsEmpty() {
		level := []int{}
		levelSize := d.Size()

		for i := 0; i < levelSize; i++ {
			node := d.PopLeft()
			level = append(level, node.Val)
			if node.Left != nil {
				d.Append(node.Left)
			}
			if node.Right != nil {
				d.Append(node.Right)
			}
		}

		levels = append(levels, level)
	}

	return levels
}

func testRun102() [][]int {
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
			},
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Right: &TreeNode{
				Val: 6,
			},
		},
	}

	res := levelOrder(root)
	return res
}
