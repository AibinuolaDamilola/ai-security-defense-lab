import streamlit as st
import json

ILLUSTRATION_MEDVITALS = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#ECFDF5"/><rect x="90" y="90" width="140" height="110" fill="#0F172A" rx="4"/><polygon points="90,90 160,50 230,90" fill="#10B981"/><rect x="150" y="58" width="20" height="20" fill="#10B981"/><rect x="142" y="66" width="36" height="6" fill="#10B981"/><rect x="110" y="120" width="24" height="24" fill="#fff"/><rect x="146" y="120" width="24" height="24" fill="#fff"/><rect x="182" y="120" width="24" height="24" fill="#fff"/><rect x="110" y="156" width="24" height="24" fill="#fff"/><rect x="146" y="156" width="24" height="24" fill="#fff"/><rect x="182" y="156" width="24" height="24" fill="#fff"/><rect x="148" y="180" width="24" height="20" fill="#94A3B8"/><polyline points="20,210 60,210 75,180 90,230 105,150 120,210 300,210" fill="none" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="245" cy="150" r="12" fill="#F1C9A6"/><rect x="233" y="162" width="24" height="40" rx="6" fill="#0EA5E9"/><circle cx="275" cy="160" r="11" fill="#E8B589"/><rect x="264" y="171" width="22" height="36" rx="6" fill="#CBD5E1"/></svg>'

CLOUDTRAIL_LOGS = [
    {"event_time": "2026-06-29 23:01:44 UTC", "event_name": "GetObject",              "source_ip": "10.0.4.22",     "user_agent": "aws-sdk-java/1.11.0",    "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-29 23:14:09 UTC", "event_name": "DescribeSecurityGroups", "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-29 23:47:33 UTC", "event_name": "GetBucketPolicy",         "source_ip": "10.0.4.22",     "user_agent": "aws-sdk-python/1.26.0",  "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 00:12:55 UTC", "event_name": "PutBucketLogging",        "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 00:51:17 UTC", "event_name": "DescribeInstances",       "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 01:03:28 UTC", "event_name": "GetObject",               "source_ip": "10.0.4.22",     "user_agent": "aws-sdk-java/1.11.0",    "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 01:22:41 UTC", "event_name": "CreateLogGroup",          "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 01:58:03 UTC", "event_name": "DescribeLogStreams",       "source_ip": "10.0.4.22",     "user_agent": "aws-sdk-python/1.26.0",  "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 02:05:19 UTC", "event_name": "ListRoles",               "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:14:11 UTC", "event_name": "ConsoleLogin",            "source_ip": "10.0.4.22",     "user_agent": "Mozilla/5.0 (Windows)",  "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:14:45 UTC", "event_name": "DescribeInstances",       "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:38:04 UTC", "event_name": "GetBucketAcl",            "source_ip": "10.0.4.22",     "user_agent": "aws-sdk-python/1.26.0",  "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 02:55:33 UTC", "event_name": "UpdateFunctionCode",      "source_ip": "10.0.4.22",     "user_agent": "aws-cli/2.13.0",         "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:02:09 UTC", "event_name": "AssumeRole",              "source_ip": "198.51.100.45", "user_agent": "python-requests/2.28.1", "identity": "medvitals-deploy-bot → arn:aws:iam::000000000000:role/AdminFullAccess"},
    {"event_time": "2026-06-30 03:02:31 UTC", "event_name": "ListBuckets",             "source_ip": "198.51.100.45", "user_agent": "python-requests/2.28.1", "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:03:02 UTC", "event_name": "PutObject",               "source_ip": "198.51.100.45", "user_agent": "python-requests/2.28.1", "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:04:18 UTC", "event_name": "",               "source_ip": "198.51.100.45", "user_agent": "python-requests/2.28.1", "identity": "medvitals-deploy-bot"},
]

CLOUDTRAIL_DETAILS = [
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/medvitals-app-role/session-prod","accountId":"000000000000","sessionContext":{"sessionIssuer":{"type":"Role","userName":"medvitals-app-prod"}}},"eventTime":"2026-06-29T23:01:44Z","eventSource":"s3.amazonaws.com","eventName":"GetObject","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-sdk-java/1.11.0","requestParameters":{"bucketName":"medvitals-patient-records","key":"configs/app_config.json"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000001","eventID":"evt-0001"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-29T23:14:09Z","eventSource":"ec2.amazonaws.com","eventName":"DescribeSecurityGroups","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"filterSet":{"items":[{"name":"vpc-id","valueSet":{"items":[{"value":"vpc-0abc1234def56789a"}]}}]}},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000002","eventID":"evt-0002"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/medvitals-app-role/session-prod","accountId":"000000000000"},"eventTime":"2026-06-29T23:47:33Z","eventSource":"s3.amazonaws.com","eventName":"GetBucketPolicy","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-sdk-python/1.26.0","requestParameters":{"bucketName":"medvitals-patient-records"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000003","eventID":"evt-0003"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T00:12:55Z","eventSource":"s3.amazonaws.com","eventName":"PutBucketLogging","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"bucketName":"medvitals-patient-records","bucketLoggingStatus":{"loggingEnabled":{"targetBucket":"medvitals-access-logs","targetPrefix":"s3-access/"}}},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000004","eventID":"evt-0004"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T00:51:17Z","eventSource":"ec2.amazonaws.com","eventName":"DescribeInstances","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"filterSet":{"items":[{"name":"instance-state-name","valueSet":{"items":[{"value":"running"}]}}]}},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000005","eventID":"evt-0005"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/medvitals-app-role/session-prod","accountId":"000000000000"},"eventTime":"2026-06-30T01:03:28Z","eventSource":"s3.amazonaws.com","eventName":"GetObject","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-sdk-java/1.11.0","requestParameters":{"bucketName":"medvitals-patient-records","key":"patient-data/intake-forms/form-00441.json"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000006","eventID":"evt-0006"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T01:22:41Z","eventSource":"logs.amazonaws.com","eventName":"CreateLogGroup","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"logGroupName":"/medvitals/api/prod"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000007","eventID":"evt-0007"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/medvitals-app-role/session-prod","accountId":"000000000000"},"eventTime":"2026-06-30T01:58:03Z","eventSource":"logs.amazonaws.com","eventName":"DescribeLogStreams","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-sdk-python/1.26.0","requestParameters":{"logGroupName":"/medvitals/api/prod","orderBy":"LastEventTime","descending":True},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000008","eventID":"evt-0008"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T02:05:19Z","eventSource":"iam.amazonaws.com","eventName":"ListRoles","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"pathPrefix":"/"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000009","eventID":"evt-0009"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T02:14:11Z","eventSource":"signin.amazonaws.com","eventName":"ConsoleLogin","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","requestParameters":None,"responseElements":{"ConsoleLogin":"Success"},"errorCode":None,"requestID":"A1B2C3000010","eventID":"evt-0010"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T02:14:45Z","eventSource":"ec2.amazonaws.com","eventName":"DescribeInstances","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"filterSet":{"items":[{"name":"instance-state-name","valueSet":{"items":[{"value":"running"}]}}]}},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000011","eventID":"evt-0011"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/medvitals-app-role/session-prod","accountId":"000000000000"},"eventTime":"2026-06-30T02:38:04Z","eventSource":"s3.amazonaws.com","eventName":"GetBucketAcl","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-sdk-python/1.26.0","requestParameters":{"bucketName":"medvitals-patient-records"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000012","eventID":"evt-0012"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T02:55:33Z","eventSource":"lambda.amazonaws.com","eventName":"UpdateFunctionCode","awsRegion":"us-east-1","sourceIPAddress":"10.0.4.22","userAgent":"aws-cli/2.13.0","requestParameters":{"functionName":"medvitals-triage-processor","s3Bucket":"medvitals-deployments","s3Key":"lambda/triage-processor-v2.4.1.zip"},"responseElements":{"functionName":"medvitals-triage-processor","lastModified":"2026-06-30T02:55:34.000Z"},"errorCode":None,"requestID":"A1B2C3000013","eventID":"evt-0013"},
    {"eventVersion":"1.08","userIdentity":{"type":"IAMUser","arn":"arn:aws:iam::000000000000:user/medvitals-deploy-bot","accountId":"000000000000","userName":"medvitals-deploy-bot"},"eventTime":"2026-06-30T03:02:09Z","eventSource":"sts.amazonaws.com","eventName":"AssumeRole","awsRegion":"us-east-1","sourceIPAddress":"198.51.100.45","userAgent":"python-requests/2.28.1","requestParameters":{"roleArn":"arn:aws:iam::000000000000:role/AdminFullAccess","roleSessionName":"automation-session-1751249729","durationSeconds":3600},"responseElements":{"credentials":{"accessKeyId":"ASIA-TEMP-SESSION-KEY-9988","expiration":"2026-06-30T04:02:09Z","sessionToken":"[REDACTED]"},"assumedRoleUser":{"assumedRoleId":"AROAT4ADMINROLEID:automation-session-1751249729","arn":"arn:aws:sts::000000000000:assumed-role/AdminFullAccess/automation-session-1751249729"}},"errorCode":None,"requestID":"A1B2C3000014","eventID":"evt-0014"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/AdminFullAccess/automation-session-1751249729","accountId":"000000000000","sessionContext":{"sessionIssuer":{"type":"Role","arn":"arn:aws:iam::000000000000:role/AdminFullAccess","userName":"AdminFullAccess"}}},"eventTime":"2026-06-30T03:02:31Z","eventSource":"s3.amazonaws.com","eventName":"ListBuckets","awsRegion":"us-east-1","sourceIPAddress":"198.51.100.45","userAgent":"python-requests/2.28.1","requestParameters":None,"responseElements":{"buckets":{"items":[{"name":"medvitals-patient-records","creationDate":"2025-11-14T09:22:31.000Z"},{"name":"medvitals-deployments","creationDate":"2025-11-14T09:23:05.000Z"},{"name":"medvitals-access-logs","creationDate":"2025-11-14T09:23:44.000Z"},{"name":"medvitals-model-weights","creationDate":"2026-01-08T14:11:22.000Z"}]}},"errorCode":None,"requestID":"A1B2C3000015","eventID":"evt-0015"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/AdminFullAccess/automation-session-1751249729","accountId":"000000000000"},"eventTime":"2026-06-30T03:03:02Z","eventSource":"s3.amazonaws.com","eventName":"PutObject","awsRegion":"us-east-1","sourceIPAddress":"198.51.100.45","userAgent":"python-requests/2.28.1","requestParameters":{"bucketName":"medvitals-patient-records","key":"__exfil__/bulk-export-20260630.tar.gz","x-amz-server-side-encryption":"None"},"responseElements":{"x-amz-id-2":"EXAMPLE123456789","ETag":"\"d41d8cd98f00b204e9800998ecf8427e\""},"errorCode":None,"requestID":"A1B2C3000016","eventID":"evt-0016"},
    {"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::000000000000:assumed-role/AdminFullAccess/automation-session-1751249729","accountId":"000000000000"},"eventTime":"2026-06-30T03:04:18Z","eventSource":"s3.amazonaws.com","eventName":"GetObject","awsRegion":"us-east-1","sourceIPAddress":"198.51.100.45","userAgent":"python-requests/2.28.1","requestParameters":{"bucketName":"medvitals-patient-records","key":"__exfil__/bulk-export-20260630.tar.gz"},"responseElements":None,"errorCode":None,"requestID":"A1B2C3000017","eventID":"evt-0017"},
]


def render_cloudtrail_table(student_email):
    def esc(s):
        return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

    cols = "200px 170px 148px 195px 1fr"

    style = (
        '<style>'
        'details.ct-row>summary{list-style:none;display:grid;grid-template-columns:' + cols + ';cursor:pointer;}'
        'details.ct-row>summary::-webkit-details-marker{display:none;}'
        'details.ct-row>summary::marker{display:none;}'
        'details.ct-row>summary:hover .ct-cell{background:#1C2128;}'
        'details.ct-row[open]>summary .ct-arr{color:#A7F3D0;}'
        '</style>'
    )

    out = (
        '<div style="background:#0D1117;border:1px solid #30363D;border-radius:8px;overflow:hidden;margin-top:16px;">'
        '<div style="background:#161B22;padding:12px 20px;border-bottom:1px solid #30363D;display:flex;justify-content:space-between;align-items:center;">'
        '<div style="color:#58A6FF;font-weight:600;font-size:14px;">CloudTrail — Event History</div>'
        '<div style="color:#8B949E;font-size:12px;">Filter: Last 24 hours &nbsp;·&nbsp; Region: us-east-1</div>'
        '</div>'
        f'<div style="display:grid;grid-template-columns:{cols};background:#161B22;border-bottom:1px solid #30363D;">'
        '<div style="padding:10px 16px;color:#8B949E;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;">Event Time</div>'
        '<div style="padding:10px 16px;color:#8B949E;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;">Event Name</div>'
        '<div style="padding:10px 16px;color:#8B949E;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;">Source IP</div>'
        '<div style="padding:10px 16px;color:#8B949E;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;">User Agent</div>'
        '<div style="padding:10px 16px;color:#8B949E;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;">Identity / Resource</div>'
        '</div>'
    )

    for log, detail in zip(CLOUDTRAIL_LOGS, CLOUDTRAIL_DETAILS):
        json_str = json.dumps(detail, indent=2, default=str)
        json_esc = esc(json_str)
        out += (
            '<details class="ct-row" style="border-bottom:1px solid #21262D;">'
            '<summary>'
            f'<div class="ct-cell" style="padding:10px 16px;color:#8B949E;font-family:monospace;font-size:12px;"><span class="ct-arr" style="color:#6366F1;margin-right:5px;">▶</span>{log["event_time"]}</div>'
            f'<div class="ct-cell" style="padding:10px 16px;color:#58A6FF;font-family:monospace;font-size:12px;">{log["event_name"]}</div>'
            f'<div class="ct-cell" style="padding:10px 16px;color:#E6EDF3;font-family:monospace;font-size:12px;">{log["source_ip"]}</div>'
            f'<div class="ct-cell" style="padding:10px 16px;color:#8B949E;font-family:monospace;font-size:12px;">{log["user_agent"]}</div>'
            f'<div class="ct-cell" style="padding:10px 16px;color:#E6EDF3;font-family:monospace;font-size:12px;word-break:break-all;">{esc(log["identity"])}</div>'
            '</summary>'
            '<div style="background:#FFFFFF;border-top:1px solid #30363D;padding:16px 20px;">'
            f'<pre style="color:#1E293B;font-size:11px;line-height:1.7;margin:0;white-space:pre-wrap;font-family:Consolas,Monaco,monospace;">{json_esc}</pre>'
            '</div>'
            '</details>'
        )

    out += (
        f'<div style="padding:8px 16px;background:#161B22;color:#8B949E;font-size:11px;border-top:1px solid #30363D;">'
        f'Showing {len(CLOUDTRAIL_LOGS)} events &nbsp;·&nbsp; Student: {student_email}</div>'
        '</div>'
    )

    st.markdown(style + out, unsafe_allow_html=True)


def render_level1(user, supabase_client):

    if not st.session_state.get("l1_completed"):
        try:
            result = supabase_client.table("defense_lab_progress").select("completed").eq(
                "user_id", str(user.id)
            ).eq("level_number", 1).execute()
            if result.data and result.data[0].get("completed"):
                st.session_state.l1_completed = True
        except Exception:
            pass
            

    st.markdown(
        '<div style="background:linear-gradient(135deg,#0B7B6E,#064E3B);border-radius:10px;padding:20px 28px;margin-bottom:24px;">'
        '<div style="color:#A7F3D0;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;">Level 1 · Cloud Infrastructure Security</div>'
        '<div style="color:#fff;font-size:15px;margin-bottom:10px;"><strong>Guiding Question:</strong> How do attackers get into AI systems through infrastructure — and how do defenders trace and stop them?</div>'
        '<div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:12px;">'
        '<div><div style="color:#A7F3D0;font-size:11px;font-weight:600;margin-bottom:4px;">HEADLINE TOOLS</div><div style="color:#fff;font-size:13px;">AWS CloudTrail · Python-dotenv · IAM Policy Analyzer · GitHub</div></div>'
        '<div><div style="color:#A7F3D0;font-size:11px;font-weight:600;margin-bottom:4px;">ROLES UNLOCKED</div><div style="color:#fff;font-size:13px;">Junior Cloud Security Engineer · SOC Analyst Tier 1 · Junior DevSecOps</div></div>'
        '</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#0F172A 0%,#1E293B 100%);padding:18px 32px;border-radius:8px;display:flex;justify-content:space-between;align-items:center;margin-bottom:28px;">'
        '<div style="color:#fff;font-size:22px;font-weight:700;">MedVitals AI</div>'
        '<div style="color:#E5E7EB;font-size:13px;">Patient Login &nbsp;&nbsp;&nbsp;&nbsp; Provider Access</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            '<div style="font-size:32px;font-weight:800;color:#0F172A;line-height:1.3;">Healthcare, connected<br>and compromised.</div>'
            '<div style="font-size:14px;color:#475569;margin-top:12px;max-width:420px;">An intentionally vulnerable AI triage platform. Your job is to find the breach, trace it in the logs, and harden the infrastructure before the next attack.</div>',
            unsafe_allow_html=True,
        )
        with st.expander("📋 View Scenario Brief"):
            st.markdown(
                "**The Company**\n\nMedVitals AI is a HealthTech startup that allows patients to text an AI triage nurse. "
                "Their platform processes thousands of clinical conversations daily and stores patient records in a cloud database.\n\n"
                "**What Happened**\n\nThe engineering team hardcoded live AWS credentials directly inside the Python deployment "
                "wrapper and pushed it to a public repository. The IAM service account had a wildcard policy granting full "
                "administrative access to the entire cloud account. An automated scanner harvested the credentials within hours.\n\n"
                "**Your Three Tasks**\n\n"
                "1. Parse the CloudTrail logs — identify the exact indicator of compromise and write an Incident Timeline Report.\n"
                "2. Fix the credential exposure — move secrets to environment variables.\n"
                "3. Rewrite the IAM policy to enforce Principle of Least Privilege."
            )
    with col2:
        st.markdown(ILLUSTRATION_MEDVITALS, unsafe_allow_html=True)

    st.markdown("---")

    v1, v2, v3 = st.columns(3)
    v1.metric("Heart Rate", "72 BPM", "Stable")
    v2.metric("Blood Oxygen", "98%", "Normal")
    v3.metric("Patients Active", "1,204", "+12 today")

    st.markdown("---")

    st.markdown("#### Deployment Repository")
    st.caption("The following files were found in the MedVitals AI GitHub repository.")
    tab1, tab2 = st.tabs(["config.py", "deploy-role-policy.json"])
    with tab1:
        st.code(
            '# config.py\n# MedVitals AI — Production Environment Configuration\n# Maintained by: engineering-team@medvitals.ai\n# Last updated: 2026-05-14\n\n'
            'import os\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\n'
            'APP_ENV = "production"\nAPP_NAME = "medvitals-ai"\nAPP_PORT = 8080\nLOG_LEVEL = "INFO"\n\n'
            'AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")\n'
            'AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")\n'
            'AWS_ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")\n\n'
            'DB_HOST = os.environ.get("DB_HOST")\n'
            'DB_PORT = int(os.environ.get("DB_PORT", 5432))\n'
            'DB_NAME = os.environ.get("DB_NAME")\n'
            'DB_USER = os.environ.get("DB_USER")\n'
            'DB_PASSWORD = os.environ.get("DB_PASSWORD")\n\n'
            'LLM_ENDPOINT = os.environ.get("LLM_ENDPOINT")\n'
            'LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o")\n'
            'LLM_TIMEOUT = int(os.environ.get("LLM_TIMEOUT", 30))\n\n'
            'SESSION_SECRET = os.environ.get("SESSION_SECRET")',
        )
    with tab2:
        st.code(
            '{\n'
            '  "Version": "2012-10-17",\n'
            '  "Statement": [\n'
            '    {\n'
            '      "Sid": "MedVitalsServiceRole",\n'
            '      "Effect": "Allow",\n'
            '      "Action": [\n'
            '        "s3:GetObject",\n'
            '        "s3:PutObject",\n'
            '        "logs:CreateLogGroup",\n'
            '        "logs:CreateLogStream",\n'
            '        "logs:PutLogEvents",\n'
            '        "lambda:UpdateFunctionCode",\n'
            '        "ec2:DescribeInstances",\n'
            '        "ec2:DescribeSecurityGroups"\n'
            '      ],\n'
            '      "Resource": [\n'
            '        "arn:aws:s3:::medvitals-patient-records/*",\n'
            '        "arn:aws:s3:::medvitals-deployments/*"\n'
            '      ]\n'
            '    }\n'
            '  ]\n'
            '}',
            language="json",
        )

    st.markdown("---")

    st.markdown("#### AWS CloudTrail — Event History")
    st.caption("A breach occurred last night. Click any row to expand its full JSON record. Find the indicator of compromise and write your Incident Timeline Report.")
    render_cloudtrail_table(user.email)

    st.markdown("---")

    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. Walk me through how you would investigate a suspected cloud credential compromise.\n"
            "2. What is the principle of least privilege and how would you apply it to an IAM policy?\n"
            "3. What CloudTrail fields tell you an AssumeRole attack has occurred?\n"
            "4. What is the difference between hardcoding an API key and using os.environ.get()?"
        )

    st.markdown("---")
    st.markdown("#### Submit Your Level 1 Work")

    if st.session_state.get("l1_completed"):
        st.success("✅ Level 1 is complete. Level 2 — DataForge ML is now unlocked.")
        if st.button("← Return to Hub", key="l1_return_done"):
            st.session_state.view = "hub"
            st.rerun()
        return

    st.info(
        "Before submitting, confirm all three tasks are done:\n\n"
        "1. **Identified the IoC** in CloudTrail and written your Incident Timeline Report.\n"
        "2. **Fixed the credential exposure** — moved secrets to environment variables.\n"
        "3. **Rewritten the IAM policy** to enforce Principle of Least Privilege."
    )

    commit_url = st.text_input("GitHub commit URL showing your code fix:", placeholder="https://github.com/your-username/ai-security-defense-lab/commit/abc123", key="l1_commit_url")
    report_url = st.text_input("Incident Timeline Report link (GitHub Gist, Google Doc, or Medium post):", placeholder="https://gist.github.com/your-username/...", key="l1_report_url")

    if st.button("Submit Level 1 Work →", key="l1_submit"):
        if not commit_url or not report_url:
            st.warning("Paste both links above before submitting.")
        elif "github.com" not in commit_url and "gitlab.com" not in commit_url:
            st.warning("The first link must be a GitHub or GitLab commit URL.")
        else:
            try:
                supabase_client.table("defense_lab_progress").update({"completed": True, "completed_at": "now()"}).eq("user_id", str(user.id)).eq("level_number", 1).execute()
                st.session_state.l1_completed = True
                st.rerun()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
