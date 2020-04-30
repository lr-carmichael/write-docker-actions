const core = require("@actions/core");
const github = require("@actions/github");

async function run() {
  const issueTitle = core.getInput("issueTitle");
  const catFact = core.getInput("catFact");

  const token = core.getInput("repoToken");
  try {
    const oktokit = new github.GitHub(token);

    const newIssue = await oktokit.issue.create({
      repo: github.context.repo.repo,
      owner: github.context.repo.owner,
      title: issueTitle,
      body: catFact
    });
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
##[error]oktokit is not defined