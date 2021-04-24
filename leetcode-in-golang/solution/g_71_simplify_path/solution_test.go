package g_71_simplify_path

import "testing"

func Test_simplifyPath(t *testing.T) {
	type args struct {
		path string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{name: "/home/", args: args{"/home/"}, want: "/home"},
		{name: "/../", args: args{"/../"}, want: "/"},
		{name: "/", args: args{"/"}, want: "/"},
		{name: "/.", args: args{"/."}, want: "/"},
		{name: "/.a", args: args{"/.a"}, want: "/.a"},
		{name: "/..a", args: args{"/..a"}, want: "/..a"},
		{name: "/home//foo", args: args{"/home//foo/"}, want: "/home/foo"},
		{name: "/a/./b/../../c/", args: args{"/a/./b/../../c/"}, want: "/c"},
		{name: "/a/../../b/../c//.//", args: args{"/a/../../b/../c//.//"}, want: "/c"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := simplifyPath(tt.args.path); got != tt.want {
				t.Errorf("simplifyPath() = %v, want %v", got, tt.want)
			}
		})
	}
}
