package g_71_simplify_path

import (
	"strings"
)

func simplifyPath(path string) string {
	paths := strings.Split(path, "/")
	stack := make([]string, 0, len(paths))
	for _, v := range paths {
		switch v {
		case ".", "":
			continue
		case "..":
			if len(stack) > 0 {
				stack = stack[0 : len(stack)-1]
			}

		default:
			stack = append(stack, v)
		}
	}
	return "/" + strings.Join(stack, "/")
}
