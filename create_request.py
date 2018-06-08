import git
import github3

def main():
    repo = git.Repo.init(".")
    test_git = repo.git
    test_git.checkout("-b", "test-branch")
    test_git.add("test.txt")
    test_git.commit("-m", "Test commit")
    test_git.push()

if __name__ == "__main__":
    main()