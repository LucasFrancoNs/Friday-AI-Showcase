# Security model (showcase)

The public Friday showcase demonstrates the security ideas used by the project without publishing credentials, personal data, or private integration details.

## Main controls

1. **Policy Engine** classifies actions by risk and current mode.
2. **Provenance / taint concepts** distinguish user authorization from untrusted external content.
3. **Sandbox Gate** keeps generated code away from the real project until validation.
4. **Checkpoint / rollback** protects mutations where supported.
5. **Defender** compares critical files against an integrity baseline.
6. **Circuit breakers** stop repeated failing tools/providers from consuming an entire run.
7. **Bounded context** avoids unlimited session growth.

## Secrets

Never commit `.env`, `key.env`, API keys, cookies, tokens, personal memories, logs or checkpoints. This repository contains no production credentials.

## Reporting

If you discover a security problem in this showcase, open an issue describing the affected public component. Do not include real credentials or personal data in issue content.
